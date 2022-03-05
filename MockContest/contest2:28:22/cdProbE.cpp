// Input
// The input consists of a sequence of test cases. The first line of each test case contains two positive integers 𝑁 and 𝑀, each at most one million, specifying the number of CDs owned by Jack and by Jill, respectively. This line is followed by 𝑁 lines listing the catalog numbers of the CDs owned by Jack in increasing order, and 𝑀 more lines listing the catalog numbers of the CDs owned by Jill in increasing order. Each catalog number is a positive integer no greater than one billion. The input is terminated by a line containing two zeros. This last line is not a test case and should not be processed.

// Output
// For each test case, output a line containing one integer, the number of CDs that Jack and Jill both own.

#include <iostream>
#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

int main() {
	int n, m;
	while (cin >> n >> m) 
	{
		if (!n || !m) break;
		unordered_set<int> N;
		for (int i = 0; i < n; ++i)
		{
			int num;
			cin >> num;
			N.insert(num);
		}
		int cnt = 0;
		for (int i = 0; i < m; ++i) 
		{
			int num;
			cin >> num;
			if (N.count(num)) ++cnt;
		}
	cout << endl;
	cout << cnt << endl;
	}
	return 0;
}

