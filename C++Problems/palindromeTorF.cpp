/*
 * Title: palindromeTorF.cpp
 * Abstract: Input a string, recognize if its a palindrone or not, return True or False
 * Name: Matthew Fernandez
 * Date: 2/3/2022
*/

#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main(){
    string str; // user input string
	int j; // iterator
	int tolower ( int c); // to convert to lowercase
	vector<char> forward, backward; // 2 vectors to check if palindrome
    cout << "Input Possible Palindrome: " << endl;
    cin >> str;
	transform(str.begin(), str.end(), str.begin(), tolower); // convert to lowercase
	j = str.length()-1; // used to iterate backwards
    for(int i =0; i < str.length(); i++){ // will compare each char to check for palindrome
		forward.push_back(str[i]);
		backward.push_back(str[j]);
		j--; 
    }
	for(int i =0 ; i < forward.size(); i++){
		if(forward[i] == backward[i]){ // maybe a palindrome
			if(i == forward.size()-1){ //iterated through all chars, definitely a palindrome
				cout << "True, this is a palindrome"<< endl;
			}
		}else{
			cout << "False, this is not a palindrome"<<endl;
			break;
		}
	}
	return 0;
}

