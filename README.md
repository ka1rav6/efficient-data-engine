# Efficient Data Engine

> A high-performance **command-line data processing engine** powered by a **C++ computation core** and a **Python interface**.

Efficient Data Engine performs **matrix operations, statistical analysis, sorting, and CSV dataset exploration**.  
All heavy data processing is handled by a **C++ backend** for speed, while Python provides a simple command-line interface.

---

# Architecture

The system is designed with a **hybrid architecture**:

```
Python Interface  ->  pybind11  ->  C++ Core Engine
```

- **C++ Core (`cpp_core/`)**
  - Handles all computation
  - Matrix operations
  - Statistical calculations
  - Sorting algorithms
  - CSV data processing

- **Python Interface**
  - Command-line interaction
  - User input processing
  - File handling

The integration between Python and C++ is implemented using **pybind11**, allowing Python to directly call optimized C++ functions.

The project is built using **CMake**, which compiles the C++ core and generates the Python bindings.

---

# Features

## Matrix Operations

- Matrix Multiplication
- Matrix Addition
- Matrix Subtraction
- Supports operations on **multiple matrices**

---

## Statistical Calculations

The engine supports common statistical functions:

- Mean
- Median
- Mode
- Standard Deviation
- Variance
- Minimum
- Maximum
- Range
- Z-score
- Percentile

Input formats supported:

- **Space-separated values**
- **Comma-separated values**

Example:

```
mean 10 20 30 40 50
```

or

```
mean 10,20,30,40,50
```

---

## Sorting Algorithms

Implemented sorting algorithms:

- Quick Sort
- Insertion Sort
- Bubble Sort

Example:

```
quicksort int 9 3 7 1 5
```

---

# CSV File Analysis

The engine can load a CSV file and perform statistical operations on its columns.

## CSV Format

- First row -> **column labels**
- Remaining rows -> **numeric data**
- Labels **must not contain spaces**

Example:

```
age,height,weight
20,170,65
22,180,72
19,165,60
```

---

# Commands

## General Notes

- `datatype` -> `int` or `float`
- `data` -> space-separated or comma-separated values

---

# Normal Mode Commands

| Command | Description |
|------|-------------|
| `matmul datatype number_of_matrices` | Multiply matrices |
| `mean data` | Mean of dataset |
| `median data` | Median of dataset |
| `mode data` | Mode |
| `std_dev data` | Standard deviation |
| `var data` | Variance |
| `min data` | Minimum value |
| `max data` | Maximum value |
| `range data` | Range |
| `zscore value data` | Z-score |
| `percentile value data` | Percentile |
| `clear` or `cls` | Clear screen |
| `help` | Display commands |

---

# Sorting Commands

| Command | Description |
|------|-------------|
| `quicksort datatype data` | Quick Sort |
| `insertionsort datatype data` | Insertion Sort |
| `bubblesort datatype data` | Bubble Sort |

Example:

```
insertionsort float 3.2 5.1 1.8 7.4
```

---

# File Mode

Enter file mode using:

```
load
```

You will be prompted to enter the **CSV file path**.

---

## File Mode Commands

| Command | Description |
|------|-------------|
| `mean` | Mean for all columns |
| `mean label` | Mean of a specific column |
| `median` | Median for all columns |
| `median label` | Median of a specific column |
| `display` | Display full dataset |
| `display label` | Display a specific column |
| `file.close` | Exit file mode |

---

# Example Workflow

```
load
Enter file path: data.csv

mean
mean height
median weight
display
display age

file.close
```

---

# Project Structure

```
efficient-data-engine
│
├── cpp_core
│   ├── normal_data.cpp
│   ├── fileProcessing.cpp
│   └── sorting.cpp
│
├── py_interface
│   ├── main.py
│   └── inputProcessing.py
│
├── testcases
│   ├── test1.csv
│   └── test2.csv
│
├── CMakeLists.txt
└── README.md
```

---

# Testcases

The **`testFiles`** folder contains **two CSV files** that can be used to test the file analysis functionality of the engine.

These files demonstrate:

- CSV loading
- Statistical analysis on columns
- Dataset display functionality

---

# Build System

The project uses **CMake** to build the C++ core and generate Python bindings.

### Requirements

- Python
- C++ Compiler
- CMake
- pybind11

---

# Building the Project

Example build process:

```
mkdir build
cd build
cmake ..
make
```

This will compile the **C++ computation engine** and generate the Python module used by the CLI interface.

---

# Goals of the Project

- Implement **core data analysis algorithms from scratch**
- Explore **C++ + Python interoperability**
- Build a **high-performance computation engine**
- Practice **pybind11 bindings and CMake builds**

---

# Future Improvements

- Additional matrix operations
- Matrix Resizing
- More statistical functions
- Support for larger datasets
- Performance optimizations
- Visualization tools in python

---

# License

This project is licensed under the **MIT License**.

---

# Author

**Kairav Dutta**