#include <vector>
using namespace std;
#ifndef NORMAL_DATA_H
#define NORMAL_DATA_H

double sum(const vector<double> &arr);
double mean(const vector<double> &arr);
double median(vector<double> arr);
double mode(vector<double> arr);
double var(const vector<double> &arr);
double mini(const vector<double> &A);
double maxi(const vector<double> &A);
double range(const vector<double> &A);
double percentile(const vector<double> &A, double val);
double zscore(const vector<double> &A, double val);
double std_dev(const vector<double> &arr);
vector<double> matrixMultiply(const vector<double> &A, const vector<double>& B, int n);
vector<double> matrixAdd(const vector<double> &A, const vector<double> &B, int r, int c);
vector<double> matrixSubtract(const vector<double> &A, const vector<double> &B, int r, int c);

#endif