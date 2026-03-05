#include <vector>

#ifndef NORMAL_DATA_H
#define NORMAL_DATA_H

double sum(const std::vector<double> &arr);
double mean(const std::vector<double> &arr);
double median(std::vector<double> arr);
double mode(std::vector<double> arr);
double var(std::vector<double> &arr);
double std_dev(std::vector<double> &arr);
std::vector<double> matrixMultiply(const std::vector<double> &A, const std::vector<double>& B, int n);
#endif