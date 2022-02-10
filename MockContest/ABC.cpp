#include <iostream>
#include <vector>
#include <bits/stdc++.h> 

using namespace std;

int main(){
    char x, y , z;
    int int1, int2, int3;
    vector<int> ABC, outputVals, sortedVals;
    cin >> int1 >> int2 >> int3;
    cin >> x >> y >> z;    
    ABC.push_back(x);
    ABC.push_back(y);
    ABC.push_back(z);

    sortedVals.push_back(int1);
    sortedVals.push_back(int2);
    sortedVals.push_back(int3);
    sort(sortedVals.begin(), sortedVals.end());

	for (int i =0; i <3; i++){
		if(ABC[i] == 'A'){
			outputVals.push_back(sortedVals[0]);
		}else if(ABC[i] == 'B'){
       		outputVals.push_back(sortedVals[1]);
		}else if(ABC[i] == 'C'){
       		outputVals.push_back(sortedVals[2]);
		}
	}
    for(int i=0; i <=outputVals.size();i++){
        if(i == outputVals.size()-1){
            cout << outputVals[i] << endl;
			break;
        }
        cout << outputVals[i] << " ";
    }
    return 0;
}