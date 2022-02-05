/*
Author: Matthew Fernandez
Abstract: Input consists of up to 10000 integers, one per line. Each is in
the range [0,1000000]. Input ends at end of file.

For each integer 𝑛, print the number of digits required to represent 𝑛! in base-10.
Date: 2/4/2022
*/
#include <iostream>
#include <vector>
#include <math.h>
#include <string> 
#include <sstream>

using namespace std;

int main(){

	float N=0;
	string line;
	vector<int> allN;
	vector<int> int_N; // will use to truncate float to int 

	while(true){ // read in all N values
        if ( not getline( cin, line ) or line.empty() ) break; // if line is empty 

        try
        {
            int value = stoi( line ); // convert from str to int
            allN.push_back( value ); // add val to vector
        }
        catch ( ... ) // should be int format
        {
			break;
        }           
	}
	for (int j =0; j>allN.size()-1; j++) {// loop through all element in vector
		for( int i=2; i >= allN[j]+1; i++){ // from 1 to N do log arithmatic
			N = N + log(i); 
		}
		// TODO: Below has a bug, FIX IT
		int_N.push_back(N); // truncate from float to int
		int val = int_N[j] + 1;
		cout << val << endl;
	}
	return 0;
}
