#include <iostream>
#include <vector>
using namespace std;
template <typename T>
auto sum(const vector<T> &arr){
    T sum =0;
    for (auto num: arr){
        sum+=num;
    }
    return sum;
}
template <typename T>
auto mean(const vector<T> &arr){
    auto summation = sum(arr); 
    return summation/((double)arr.size());
}
template <typename T>
auto median(vector<T> arr) {  // pass by value (copy)
    mergeSort(arr, 0, arr.size() - 1);

    int len = arr.size();

    if (len % 2) {  // odd
        return arr[len / 2];
    }

    return (arr[len/2 - 1] + arr[len/2]) / static_cast<double>(2);
}

template <typename T>
void mergeSort(vector<T> &arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        
        vector<T> temp;
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

template <typename T>
auto mode(vector<T> arr){
    mergeSort(arr, 0, arr.size()-1);
    int freq_max=0, freq=1;
    T max_elem= arr.at(0);
    for (int i = 1; i<arr.size(); i++){
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


int main(){
    vector<double> vec = {5.5, 2.2, 3.3, 2.2, 2.2, 1.0};
    cout << mean(vec) << endl;
    cout << median(vec) << endl;
    cout << mode(vec) << endl;
    return 0;
}