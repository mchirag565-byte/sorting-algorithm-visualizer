import random
import tkinter as tk


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.geometry("850x600")
        self.root.configure(bg="#1e1e2f")

        self.values = []
        self.sorting = False

        tk.Label(
            root,
            text="Sorting Algorithm Visualizer",
            font=("Arial", 22, "bold"),
            bg="#1e1e2f",
            fg="white",
        ).pack(pady=12)

        controls = tk.Frame(root, bg="#1e1e2f")
        controls.pack(pady=8)

        tk.Label(
            controls, text="Array size:", bg="#1e1e2f", fg="white"
        ).grid(row=0, column=0, padx=5)

        self.size = tk.IntVar(value=35)
        tk.Scale(
            controls,
            from_=10,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.size,
            bg="#1e1e2f",
            fg="white",
            highlightthickness=0,
        ).grid(row=0, column=1, padx=5)

        tk.Label(
            controls, text="Speed:", bg="#1e1e2f", fg="white"
        ).grid(row=0, column=2, padx=5)

        self.speed = tk.IntVar(value=30)
        tk.Scale(
            controls,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.speed,
            bg="#1e1e2f",
            fg="white",
            highlightthickness=0,
        ).grid(row=0, column=3, padx=5)

        self.algorithm = tk.StringVar(value="Bubble Sort")
        tk.OptionMenu(
            controls,
            self.algorithm,
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            controls,
            text="Generate Array",
            command=self.generate_array,
            bg="#4caf50",
            fg="white",
        ).grid(row=0, column=5, padx=5)

        tk.Button(
            controls,
            text="Start Sorting",
            command=self.start_sorting,
            bg="#2196f3",
            fg="white",
        ).grid(row=0, column=6, padx=5)

        self.canvas = tk.Canvas(
            root, width=800, height=400, bg="#11111b", highlightthickness=0
        )
        self.canvas.pack(pady=15)

        self.status = tk.Label(
            root,
            text="Generate an array to begin.",
            font=("Arial", 12),
            bg="#1e1e2f",
            fg="white",
        )
        self.status.pack()

        self.generate_array()

    def generate_array(self):
        if self.sorting:
            return
        self.values = [
            random.randint(10, 100)
            for _ in range(self.size.get())
        ]
        self.status.config(text="New random array generated.")
        self.draw_bars()

    def draw_bars(self, highlighted=()):
        self.canvas.delete("all")
        if not self.values:
            return

        width = 800 / len(self.values)
        max_value = max(self.values)

        for index, value in enumerate(self.values):
            x0 = index * width + 2
            x1 = (index + 1) * width - 2
            y0 = 390 - (value / max_value) * 350
            y1 = 390

            color = "#ff5252" if index in highlighted else "#4fc3f7"
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
            if len(self.values) <= 25:
                self.canvas.create_text(
                    (x0 + x1) / 2,
                    y0 - 10,
                    text=str(value),
                    fill="white",
                    font=("Arial", 8),
                )

        self.root.update_idletasks()

    def start_sorting(self):
        if self.sorting:
            return
        self.sorting = True
        self.status.config(text=f"Sorting with {self.algorithm.get()}...")
        self.sort_generator = self.get_sort_steps()
        self.animate_sort()

    def animate_sort(self):
        try:
            highlighted = next(self.sort_generator)
            self.draw_bars(highlighted)
            delay = max(1, 101 - self.speed.get())
            self.root.after(delay, self.animate_sort)
        except StopIteration:
            self.sorting = False
            self.draw_bars()
            self.status.config(text="Sorting complete!")

    def get_sort_steps(self):
        name = self.algorithm.get()

        if name == "Bubble Sort":
            yield from self.bubble_sort()
        elif name == "Selection Sort":
            yield from self.selection_sort()
        else:
            yield from self.insertion_sort()

    def bubble_sort(self):
        n = len(self.values)
        for end in range(n - 1, 0, -1):
            for index in range(end):
                yield (index, index + 1)
                if self.values[index] > self.values[index + 1]:
                    self.values[index], self.values[index + 1] = (
                        self.values[index + 1],
                        self.values[index],
                    )
                    yield (index, index + 1)

    def selection_sort(self):
        n = len(self.values)
        for start in range(n - 1):
            smallest = start
            for index in range(start + 1, n):
                yield (smallest, index)
                if self.values[index] < self.values[smallest]:
                    smallest = index
            self.values[start], self.values[smallest] = (
                self.values[smallest],
                self.values[start],
            )
            yield (start, smallest)

    def insertion_sort(self):
        for index in range(1, len(self.values)):
            current = self.values[index]
            position = index - 1

            while position >= 0 and self.values[position] > current:
                yield (position, position + 1)
                self.values[position + 1] = self.values[position]
                position -= 1

            self.values[position + 1] = current
            yield (position + 1,)


if __name__ == "__main__":
    window = tk.Tk()
    app = SortingVisualizer(window)
    window.mainloop()