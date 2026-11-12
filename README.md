# Sorting Algorithm Visualizer

A desktop application built with Python and Tkinter that animates sorting algorithms on a randomly generated array.

## Features

- Generate random arrays with 10 to 100 values.
- Adjust the animation speed.
- Choose Bubble Sort, Selection Sort, or Insertion Sort.
- Watch compared values highlighted during sorting.
- See values displayed above bars when the array has 25 elements or fewer.

## Requirements

- Python 3
- Tkinter (included with many Python installations; on some Linux distributions it may need to be installed separately)

## Run the application

From this folder, run:

```bash
python sorting_visualizer.py
```

On systems where Python is invoked as `python3`:

```bash
python3 sorting_visualizer.py
```

## How to use

1. Launch the application.
2. Set the array size and animation speed with the sliders.
3. Choose a sorting algorithm from the menu.
4. Click **Generate Array** to create a new random array.
5. Click **Start Sorting** to watch the selected algorithm run.

## Project structure

```text
SortingVisualizer/
└── sorting_visualizer.py
```

## Algorithms

| Algorithm | Average time complexity | Space complexity |
| --- | ---: | ---: |
| Bubble Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |
