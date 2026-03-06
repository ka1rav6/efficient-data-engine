#include <vector>
#include <iostream>
#include <fstream>
#include "normal_data.h"
using namespace std;
typedef vector<string> strlist;
typedef vector<double> dbllist;

strlist processLine(string line){
    string word="";
    strlist final;
    for(char ch: line){
        if (ch == ' ') continue;
        if (ch != ',') word += ch;
        else{
            final.push_back(word);
            word = "";
        }
    }
    if(!word.empty()) final.push_back(word); // Add last element
    return final;
}

strlist getLabels(string fileName){
    ifstream fp(fileName);
    if (!fp) {
        throw "File not found!";
    }
    string labelstr;
    getline(fp, labelstr);
    strlist labels = processLine(labelstr);
    fp.close();
    return labels;
}

vector<dbllist> fileHandle(string fileName){
    ifstream fp(fileName);
    if (!fp) {
        throw "File not found!";
    }
    string labelstr;
    getline(fp, labelstr);
    strlist labels = processLine(labelstr);

    string line;
    vector<dbllist> initial;
    while (getline(fp, line)){
        strlist temp = processLine(line);
        dbllist temp2;
        for (string str:temp){
            double tempvar = stod(str);
            temp2.push_back(tempvar);
        }
        initial.push_back(temp2);
    }
    fp.close();
    vector<dbllist> final;
    int numLabels = initial[0].size();
    int numRows = initial.size();

    for (int j = 0; j < numLabels; j++) {
        dbllist col;
        for (int i = 0; i < numRows; i++) {
            col.push_back(initial[i][j]);
        }
        final.push_back(col);
    }
    // final: {{label1_row}, {label2_row},...}
    return final;

}
dbllist meanWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist means;
    for (dbllist vec: finallist){
        means.push_back(mean(vec));
    }
    return means;
}
dbllist medianWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist medians;
    for (dbllist vec: finallist){
        medians.push_back(median(vec));
    }
    return medians;
}
dbllist modeWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist modes;
    for (dbllist vec: finallist){
        modes.push_back(mode(vec));
    }
    return modes;
}
dbllist varWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist vars;
    for (dbllist vec: finallist){
        vars.push_back(var(vec));
    }
    return vars;
}
dbllist std_devWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist std_devs;
    for (dbllist vec: finallist){
        std_devs.push_back(std_dev(vec));
    }
    return std_devs;
}
dbllist rangeWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist ranges;
    for (dbllist vec: finallist){
        ranges.push_back(range(vec));
    }
    return ranges;
}
dbllist miniWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist minis;
    for (dbllist vec: finallist){
        minis.push_back(mini(vec));
    }
    return minis;
}
dbllist maxiWhole(string fileName){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist maxis;
    for (dbllist vec: finallist){
        maxis.push_back(maxi(vec));
    }
    return maxis;
}
dbllist zscoreWhole(string fileName, double val){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist zscores;
    for (dbllist vec: finallist){
        zscores.push_back(zscore(vec, val));
    }
    return zscores;
}
dbllist percentileWhole(string fileName, double val){
    strlist labels = getLabels(fileName);
    vector<dbllist> finallist = fileHandle(fileName);
    dbllist percentiles;
    for (dbllist vec: finallist){
        percentiles.push_back(percentile(vec, val));
    }
    return percentiles;
}



// int main(){
//     strlist test = processLine("Hello,label 1, label 2, this");
//     for (string label:test){
//         cout << label <<endl;
//     }
// }