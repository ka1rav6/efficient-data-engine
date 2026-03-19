#!/bin/bash

set -e 

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Starting build process...${NC}"

# Check directories exist
if [ ! -d "py_interface" ]; then
    echo -e "${RED}Error: py_interface directory not found!${NC}"
    exit 1
fi

if [ ! -d "cpp_core" ]; then
    echo -e "${RED}Error: cpp_core directory not found!${NC}"
    exit 1
fi

# Step 1: Clean old .so file
echo -e "${BLUE}Cleaning old build...${NC}"
cd py_interface
rm -f data_engine*.so || true
cd ..

# Step 2: Build in cpp_core
echo -e "${BLUE}Compiling C++ core...${NC}"
cd cpp_core

if ! command -v g++ &> /dev/null; then
    echo -e "${RED}Error: g++ not found!${NC}"
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 not found!${NC}"
    exit 1
fi

g++ -O3 -Wall -shared -std=c++17 -fPIC \
    bindings.cpp sorting.cpp normal_data.cpp fileProcessing.cpp \
    $(python3 -m pybind11 --includes) \
    -o data_engine$(python3-config --extension-suffix)

# Verify build output exists
if ls data_engine*.so 1> /dev/null 2>&1; then
    echo -e "${GREEN}Build successful!${NC}"
else
    echo -e "${RED}Build failed: .so file not found!${NC}"
    exit 1
fi

# Step 3: Copy to py_interface
echo -e "${BLUE}Copying file to py_interface...${NC}"
cp data_engine*.so ../py_interface/

cd ..

echo -e "${GREEN}All done successfully! ${NC}"