#include <vector>
#include <iostream>
using namespace std;
typedef vector<string> strlist;
typedef vector<double> dbllist;

#ifndef FILEPROCESSING_H
#define FILEPROCESSING_H

strlist processLine(string line);
strlist getLabels(string fileName);
vector<dbllist> fileHandle(string fileName);
dbllist meanWhole(string fileName);
dbllist medianWhole(string fileName);
dbllist modeWhole(string fileName);
dbllist varWhole(string fileName);
dbllist std_devWhole(string fileName);

#endif