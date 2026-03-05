#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "sorting.h"
#include "normal_data.h"
namespace py = pybind11;

PYBIND11_MODULE(data_engine, m){
    m.def("quickSort", &quickSort);
    m.def("insertionSort", &insertionSort);
    m.def("bubbleSort", &bubbleSort);
    m.def("sum", &sum);
    m.def("mean", &mean);
    m.def("median", &median);
    m.def("mode", &mode);    
    m.def("var", &var);    
    m.def("std_dev", &std_dev);
    m.def("matrixMultiply", &matrixMultiply);
}
