#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

double sum(const vector<double> &arr){
    double sum =0;
    for (double num: arr){
        sum+=num;
    }
    return sum;
}
double mean(const vector<double> &arr){
    double summation = sum(arr); 
    return summation/((double)arr.size());
}
void merge_sort(vector<double> &arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort(arr, left, mid);
        merge_sort(arr, mid + 1, right);
        
        vector<double> temp;
        int i = left, j = mid + 1;
        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp.push_back(arr[i++]);
            } else {
                temp.push_back(arr[j++]);
            }
        }
        while (i <= mid) {
            temp.push_back(arr[i++]);
        }
        while (j <= right) {
            temp.push_back(arr[j++]);
        }
        for (int i = left; i <= right; i++) {
            arr[i] = temp[i - left];
        }
    }
}
double median(vector<double> arr) {  // pass by value (copy)
    merge_sort(arr, 0, arr.size() - 1);

    int len = arr.size();

    if (len % 2) {  // odd
        return arr[len / 2];
    }

    return (arr[len/2 - 1] + arr[len/2]) / static_cast<double>(2);
}

double mode(vector<double> arr){
    merge_sort(arr, 0, arr.size()-1);
    int freq_max=1, freq=1;
    double max_elem= arr.at(0);
    int len = arr.size();
    for (int i = 1; i<len; i++){
        if (arr.at(i-1)==arr.at(i)){
            freq++;
            if (freq>freq_max) {
                freq_max = freq;
                max_elem = arr.at(i);
            }
        }
        else{
            freq=1;
        }
    }
    return max_elem;    
}
double var(vector<double> &arr){
    double mean_val = mean(arr);
    double sum_sq = 0;
    for (double num : arr) {
        sum_sq += (num - mean_val) * (num - mean_val);
    }
    return sum_sq / arr.size();
}
double std_dev(vector<double> &arr){
    double varVal = var(arr);
    return sqrt(varVal);
}


vector<double> matrixMultiply(const vector<double> &A, const vector<double>& B, int n){
    if (A.size() != n * n)
        throw invalid_argument("Matrix A size does not match n x n.");
    if (B.size() != n * n)
        throw invalid_argument("Matrix B size does not match n x n.");
    
    vector<double> C(n * n, 0.0);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                C[i * n + j] += 
                    A[i * n + k] * 
                    B[k * n + j];
            }
        }
    }
    return C;
}
int main(){
    vector<double> vec = {5.5, 2.2, 3.3, 2.2, 2.2, 1.0};
    cout << mean(vec) << endl;
    cout << median(vec) << endl;
    cout << mode(vec) << endl;
    return 0;
}