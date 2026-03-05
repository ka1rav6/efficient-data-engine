cmake_minimum_required(VERSION 3.14)
project(data_engine)

set(CMAKE_CXX_STANDARD 17)

find_package(pybind11 REQUIRED)

pybind11_add_module(data_engine
    cpp_core/bindings.cpp
    cpp_core/sorting.cpp
    cpp_core/normal_data.cpp
    cpp_core/fileProcessing.cpp
)
