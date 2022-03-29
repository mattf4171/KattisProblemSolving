// In the original Tetris, the player would receive one tetromino at a time, and each tetromino would
// be chosen from among the seven possibilities independently and uniformly at random. This meant
// that any sequence of tetrominoes could appear in a game, such as numerous I tetrominoes in a row.
// Modern versions of Tetris remove these streaks by generating tetrominoes in groups of seven: The
// first seven tetrominoes in a game will be one of each of the seven different tetrominoes in a random
// order. The next seven tetrominoes will also be one of each of the seven different tetrominoes in
// a random order (possibly but not necessarily different from the ordering of the first seven). Same
// goes for the next seven, and so on and so forth. With this generator, it is still possible to get two of
// the same tetromino in a row (for example, the seventh and eighth tetrominoes in the game can be
// the same as each other), but it is not possible to get three of the same type in a row.
// Given a sequence of tetrominoes, determine whether it is possible for a modern Tetris generator to
// produce that sequence at some point in a game.

// Input
// The first line of input contains an integer t (1 ≤ t ≤ 105
// ), which is the number of test cases.
// Each of the next t lines contains a single string s (1 ≤ |s| ≤ 1,000, s ∈ {J, L, S, Z, I, O, T}
// ∗
// ). This
// string represents a sequence of tetrominoes, and is a single test case.
// The sum of the lengths of all input test cases will not exceed 105.

// Output
// For each test case, output a single line with a single integer, which is 1 if the sequence can be
// generated by a modern Tetris generator, and 0 otherwise.

#include <bits/stdc++.h>
using namespace std;

bool validFreq(unordered_map<char, int>& freq) {
	for (auto [c, f] : freq) {
		if (f >= 2) return false;
	}
	return true;
}

bool isValid(const string& s) {
	unordered_map<char, int> freq;
	vector<bool> valid(s.size(), true); // possible to reduce the space complexity to O(1)
	for (int i = 0; i < s.size(); ++i) {
		if (i>=7) --freq[s[i-7]];
		if (s[i] != '-') ++freq[s[i]];
		valid[i] = validFreq(freq);
		if (i >= 7) valid[i] = valid[i] && valid[i-7];
		if (i+7>= s.size() && valid[i]) return true; 
	}
	return false;
}

int main() {
	int t;
	cin >> t;
	while (t--) {
		string s;
		cout << isValid(s+string(6,'-')) << endl;
	}
	return 0;
}
