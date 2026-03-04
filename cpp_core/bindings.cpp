#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

int add(int a, int b) {
    return a + b;
}

PYBIND11_MODULE(data_engine, m) {
    m.def("add", &add);
} // basic for now just for testing and establishing
