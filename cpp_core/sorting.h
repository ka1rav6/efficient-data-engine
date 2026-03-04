#include <vector>

#ifndef SORTING_H
#define SORTING_H

template <typename T>
void insertionSort(std::vector<T>& arr);
template <typename T>
void bubbleSort(std::vector<T>& arr);
template <typename T>
void merge(std::vector<T>& arr, int left, int mid, int right);
template <typename T>
void mergeSort(std::vector<T>& arr, int left, int right);
template <typename T>
int partition(std::vector<T>& arr, int low, int high);
template <typename T>
void quickSort(std::vector<T>& arr, int low, int high);


#endif // SORTING_H
