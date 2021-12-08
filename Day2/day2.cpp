#include <vector>
#include <string>
#include <fstream>
#include <bits/stdc++.h>

int main () {
    int depth = 0, horizontal = 0, aim = 0;
    std::ifstream inputFile("./input.txt");
    std::string line, command, value;
     while (getline(inputFile, line)) {
        std::istringstream stringStream(line);
        stringStream >> command; stringStream >> value;
            if(command == "forward"){
                horizontal += stoi(value);  
                depth += aim * stoi(value);
            } 
            else if(command == "down") aim += stoi(value);
            else if(command == "up") aim -= stoi(value);
        }
        printf("%d\n", depth*horizontal);
    return 0;
}