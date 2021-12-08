#include <string>
#include <fstream>
#include <cmath>
#include <vector>
#include<bits/stdc++.h>
using namespace std;

int iteratorIndex, commonBit, lessCommonBit;

int calculateCommonBit(vector<string> binaryVec) {
    float unaveraged = 0;
    for(string i : binaryVec) unaveraged += i[iteratorIndex+1] - '0';
    return (int)(round(unaveraged/binaryVec.size()));
}

bool isDiffIndex(string i, int bit){
    return(i[iteratorIndex] - '0' != bit);
}

int main () {
    ifstream inputFile("./input.txt");
    string line;
    int inputLines = 0, decimalGamma = 0, decimalEpsilon = 0, decimalOxygen = 0, decimalCoScrubber = 0, iNumber;
    float unaveragedNumber[12];
    vector<string> oxygenGen, coScrubber;

    //Calculate the sum of values on each bit position
    for(inputLines = 0; getline(inputFile, line); inputLines++){
        if(line[0] == '0') oxygenGen.push_back(line); else if(line[0] == '1') coScrubber.push_back(line);
        for(int i = 0; i < line.length(); i++) {
            unaveragedNumber[i] += line[i] - '0';
        }
    }
    //Calculate Decimal and Gamma and Epsilon, and the less and most common second bit
    for (int i=0; i < 12; i++) {
        iNumber = (int)(round(unaveragedNumber[i]/inputLines));
        decimalGamma += iNumber *pow(2, 11-i); 
        iNumber ^= 1UL << 0; decimalEpsilon += iNumber*pow(2, 11-i);
    }
    cout << "First Exercise: " << decimalGamma*decimalEpsilon << endl;

    commonBit = (iNumber = (int)(round(unaveragedNumber[1]/inputLines))); 
    iNumber ^= 1UL << 0; lessCommonBit = iNumber;
    
    for(iteratorIndex = 1; iteratorIndex < 12; iteratorIndex++) {
        if(oxygenGen.size() != 1) {
            oxygenGen.erase(std::remove_if(oxygenGen.begin(), oxygenGen.end(), [](string p) { return isDiffIndex(p, commonBit);}), oxygenGen.end());
            commonBit = calculateCommonBit(oxygenGen);
        }
        if(coScrubber.size() != 1) {
            coScrubber.erase(std::remove_if(coScrubber.begin(), coScrubber.end(), [](string p) { return isDiffIndex(p, lessCommonBit);}), coScrubber.end());
            lessCommonBit = calculateCommonBit(coScrubber); lessCommonBit ^= 1UL << 0;
        }
    }
    for (int i=0; i < 12; i++) {
        decimalOxygen += (oxygenGen[0][i] - '0')*pow(2, 11-i);
        decimalCoScrubber += (coScrubber[0][i] - '0')*pow(2, 11-i);
    }
    printf("Second Exercise: %d\n", decimalOxygen*decimalCoScrubber);
    return 0;
}