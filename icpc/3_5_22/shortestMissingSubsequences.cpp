#include <iostream>
#include <unordered_set>
#include <list>
#include <vector>
using namespace std;


bool is_subsequence(const string& strToQuery, const string& currQuery) {
    int matchIndex = 0;
	// compare with other missing subsequences to find the shortest
    for ( char k : strToQuery){
        if (currQuery[matchIndex] == k) {
            matchIndex++;
        }
        if (matchIndex == currQuery.size()) {
            return true;
        }
    }
    return false;
}

int main() {
    list<char> charSet;
    string s;
    cin >> s;
    for (char ch : s){
        charSet.push_back(ch);
    }
    string strToQuery;
    int query_num;

	cin >> strToQuery >> query_num;

    pair<int, int> min_subsequence = make_pair(-1, -1);
    for (int i = 0; i < query_num; i++) {
        string currQuery;
        cin >> currQuery;

		if (!is_subsequence(strToQuery, currQuery) && (min_subsequence.second == -1 || min_subsequence.second > currQuery.size())){
            min_subsequence.second = (int) currQuery.size();
            min_subsequence.first = i;
        }
    }

    for (int i = 0; i < query_num; i++) {
        if (i == min_subsequence.first) {
            cout << 1;
        } else {
            cout << 0;
        }
        cout << endl;
    }
	return 0;
}


// abc
// abcccabac
// 3
// cbb
// cbba
// cba




