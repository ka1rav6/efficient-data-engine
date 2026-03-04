#include <vector>
#include <algorithm>
using namespace std;

/* ---------- INSERTION SORT ---------- */

vector<double> insertionSort(vector<double> arr) {
    int n = arr.size();
    for (int i = 1; i < n; i++) {
        double key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}
/* ---------- BUBBLE SORT --------*/
std::vector<double> bubbleSort(std::vector<double> arr) {
    int n = arr.size();
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1])
                std::swap(arr[j], arr[j+1]);
        }
    }
    return arr;
}
/* ---------- QUICK SORT ---------- */

int partition(vector<double>& arr, int low, int high) {
    double pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quickSortInternal(vector<double>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSortInternal(arr, low, pi - 1);
        quickSortInternal(arr, pi + 1, high);
    }
}

vector<double> quickSort(vector<double> arr) {
    if (!arr.empty())
        quickSortInternal(arr, 0, arr.size() - 1);
    return arr;
}