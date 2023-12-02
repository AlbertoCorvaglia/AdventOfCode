#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    string line;
    int sum = 0;
    for(int id = 1; id <= 100; id++){
        getline(cin,line);
        line = line.substr(line.find(":")+2);
        bool isValid = true;
        string num;
        int nCube;
        for(int i = 0; i < (int)line.length()-2; i++){
                num="";
                if(isdigit(line[i])){
                    while(isdigit(line[i])){
                        num+=line[i];
                        i++;
                    }
                    nCube = stoi(num);
                    if(line[i+(int)num.length()-1] == 'b' && nCube > 14){
                        isValid = false;
                        break;
                    }
                    if(line[i+(int)num.length()-1] == 'g' && nCube > 13){
                        isValid = false;
                        break;
                    }
                    if(line[i+(int)num.length()-1] == 'r' && nCube > 12){
                        isValid = false;
                        break;
                    }
                }
        }
        if(isValid) sum+=id;
    }

    cout << sum;

    return 0;
}