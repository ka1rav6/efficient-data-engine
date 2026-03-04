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
auto median(const vector<T> &arr){
    int len = arr.size();
    if (len%2){ //odd
        return arr.at(1+(len/2));
    } 
    return (arr.at(len/2) + arr.at(1+(len/2)))/2;
}

template <typename T>
auto mode(const vector<T> &arr){
    
}


int main(){
    vector<double> vec = {5.5, 3.3, 2.2, 1.0};
    cout << mean(vec) << endl;
    cout << median(vec) << endl;
    return 0;
}