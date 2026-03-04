#include <vector>

#ifndef SORTING_H
#define SORTING_H

std::vector<double>  insertionSort(std:: vector<double> arr);
std::vector<double>  bubbleSort(std:: vector<double> arr);
int partition(std:: vector<double> arr, int low, int high);
std::vector<double>  quickSort(std:: vector<double> arr);


#endif // SORTING_H
