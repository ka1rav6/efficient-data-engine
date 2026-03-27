# Efficient Data Engine

> A high-performance **command-line data processing engine** powered by a **C++ computation core** and a **Python interface**, now extended with a **Tkinter GUI**.

Efficient Data Engine performs **matrix operations, statistical analysis, sorting, and CSV dataset exploration**.  
All heavy data processing is handled by a **C++ backend** for speed, while Python provides both a **CLI and GUI interface**.

---

# Architecture

The system is designed with a **hybrid architecture**:

Python Interface  ->  pybind11  ->  C++ Core Engine

- **C++ Core (`cpp_core/`)**
  - Handles all computation
  - Matrix operations
  - Statistical calculations
  - Sorting algorithms
  - CSV data processing

- **Python Interface (`py_interface/`)**
  - Command-line interaction
  - GUI interaction (Tkinter)
  - User input processing
  - File handling

The integration between Python and C++ is implemented using **pybind11**, allowing Python to directly call optimized C++ functions.

The project is built using **CMake**, which compiles the C++ core and generates the Python bindings.

---

# GUI (New Update 🚀)

A **Tkinter-based GUI (`app.py`)** has been added on top of the CLI system.

### Why this matters

- Makes the tool easier to use without terminal knowledge  
- Provides a visual interface for interaction  
- Reuses existing backend logic (no duplication)

### How to run GUI

```bash
python py_interface/app.py
```

---

# Features

## Matrix Operations

- Matrix Multiplication
- Matrix Addition
- Matrix Subtraction
- Supports operations on **multiple matrices**

---

## Statistical Calculations

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

---

## Sorting Algorithms

- Quick Sort
- Insertion Sort
- Bubble Sort

---

# CSV File Analysis

Supports CSV-based dataset exploration with column-wise operations.

---

# Commands

## Normal Mode

- matmul datatype number_of_matrices  
- mean data  
- median data  
- mode data  
- std_dev data  
- var data  
- min data  
- max data  
- range data  
- zscore value data  
- percentile value data  

---

## Sorting Commands

- quicksort datatype data  
- insertionsort datatype data  
- bubblesort datatype data  

---

# File Mode

Use:

load

Then input CSV path.

---

# Project Structure

efficient-data-engine
│
├── cpp_core
│   ├── normal_data.cpp
│   ├── fileProcessing.cpp
│   └── sorting.cpp
│
├── py_interface
│   ├── main.py
│   ├── app.py
│   └── inputProcessing.py
│
├── testcases
│   ├── test1.csv
│   └── test2.csv
│
├── CMakeLists.txt
└── README.md

---

# Build System

Run:

```bash
./compile.sh
```

---

# Requirements

- Python  
- C++ Compiler  
- CMake  
- pybind11  

---

# Goals

- Learn C++ + Python interoperability  
- Build high-performance systems  
- Practice CMake and bindings  

---

# License

MIT License

---

# Author

Kairav Dutta
