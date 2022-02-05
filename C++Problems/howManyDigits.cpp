#include <iostream>
#include <vector>
#include <math.h>
#include <string> 
#include <sstream>

using namespace std;

int main(){

	float N=0, input;
	int i;
	vector<int> allN;
	vector<int> int_N; // will use to truncate float to int 

	while(true){ // read in all N values
		cin >> input;
		// TODO: figure out how to make logic work for newline that does not contain int
		if(i == '\n'){ // condition to check if the new line contains an int or is empty
			break;
		}
		allN.push_back(input);
	}
	for (int j =0; j>allN.size()-1; j++) {// loop through all element in vector
		for( int i=1; i >= allN[j]+1; i++){ // from 1 to N do log arithmatic
			N = N + log(i); 
		}
		int_N.push_back(N); // truncate from float to int
		int val = int_N[j] + 1;
		cout << val << endl;
	}

	return 0;
}