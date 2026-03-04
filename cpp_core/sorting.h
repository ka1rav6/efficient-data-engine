#include <vector>

#ifndef SORTING_H
#define SORTING_H

void insertionSort(std::vector<double>& arr);
void bubbleSort(std::vector<double>& arr);
void merge(std::vector<double>& arr, int left, int mid, int right);
void mergeSort(std::vector<double>& arr, int left, int right);
int partition(std::vector<double>& arr, int low, int high);
void quickSort(std::vector<double>& arr, int low, int high);


#endif // SORTING_H
