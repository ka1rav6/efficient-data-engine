#!/bin/bash

set -e 

echo "Starting compile and build process..."

# Step 1: Go into py_interface and delete old .so file
cd py_interface
echo "Removing old shared object..."
rm -f data_engine.cpython-312-x86_64-linux-gnu.so

# Step 2: Go back to root directory
cd ..

# Step 3: Go into cpp_core and build
cd cpp_core
echo "Compiling C++ core..."

g++ -O3 -Wall -shared -std=c++17 -fPIC \
    bindings.cpp sorting.cpp normal_data.cpp fileProcessing.cpp \
    $(python3 -m pybind11 --includes) \
    -o data_engine$(python3-config --extension-suffix)

# Step 4: Copy the built file to py_interface
echo "Copying built file to py_interface..."
cp data_engine*.so ../py_interface/

echo "Build and copy completed successfully!"