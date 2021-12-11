#include <vector>
#include <string>
#include <fstream>
std::vector<int> inputVector;

int depth(int jump) {
    int previous = 0, increase = 0, current = 0;
    for(int i = 0; i < inputVector.size() + jump; i++, current = 0) {
        for(int j = 0; j < jump; j++) current += inputVector[i+j];
        if(previous < current && i != 0) increase++;
        previous =  current;
    }
    return increase;
}

int main () {
    std::ifstream inputFile("./input.txt");
    std::string line;
     while (getline(inputFile, line)) inputVector.push_back(stoi(line));
    printf("%d\n", depth(1));
    printf("%d\n", depth(3));
    return 0;
}