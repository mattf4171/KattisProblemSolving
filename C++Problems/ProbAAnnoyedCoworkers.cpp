// It’s another day in the office, and you’re a mastermind of not doing any work yourself. Instead, you’ll go to your coworkers for “help,” but secretly have them do all the work.

// You’ve determined that the more one of your coworkers helps you, the more annoyed they become. You’ve also been able to determine how much more annoyed a coworker gets everytime you ask them for help. At the beginning of the day, a coworker is initially 𝑎 annoyed at you. That’s their annoyance level. Everytime you ask them for help though, they become 𝑑 more annoyed at you – their annoyance level 𝑎 increases by a constant amount 𝑑 so that 𝑎=𝑎+𝑑.

// You want to complete a project of ℎ tasks solely with “help” from your coworkers, but you need to be careful not to annoy any of them too much.

// What’s the best you can do?

// Input
// The first line contains 2 integers ℎ and 𝑐, where ℎ (1≤ℎ≤100000) is the number of times you have to ask for help to complete the project, and 𝑐 (1≤𝑐≤100000) denotes the number of coworkers you have.

// Each of the following 𝑐 lines contains two positive integers 𝑎 and 𝑑, representing a coworker whose initial annoyance level is 𝑎 and who is getting more annoyed at you by an increase of 𝑑 every time you ask them for help (1≤𝑎,𝑑≤109).

// Output
// Output a single number, which is the maximum annoyance level any coworker has at you provided you use an optimal strategy to minimize this level. (In other words, of all possible strategies, choose one that minimizes the annoyance level of the worker or workers who are most annoyed at you at the end.)

// Sample Input 1 Explanation
// You have 4 coworkers and you need to ask for help 4 times. Initially, their annoyance levels are 𝑎1=1,𝑎2=2,𝑎3=3,𝑎4=4, the increases are 𝑑1=2,𝑑2=3,𝑑3=4,𝑑4=5. One optimal solution is to ask for help twice from coworker 1, once from coworker 2, and once from coworker 3, in which case the final annoyance levels are: 𝑎1=1+2⋅2=5,𝑎2=2+3=5,𝑎3=3+4=7,𝑎4=4. The coworker that is most annoyed at you is coworker 3, whose annoyance level at you is 7. Or, you could ask coworker 1 for help 3 times and coworker 2 once, leaving you with 𝑎1=1+3⋅2=7,𝑎2=2+3=5,𝑎3=3,𝑎4=4. Both strategies yield the same minimal maximum amount.
#include<bits/stdc++.h>

int main(){
    int h, c, a, d;
    vector<vector<int>> values; 
    cin >> h >> c ;
    while(h++){
        vector<int> tempVals;
        cin >> a;
        cin >> d;
        tempVals.push_back(a);
        tempVals.push_back(b);
        values.push_back(tempVals);
        h--;
    }
    for(int i=0; i<values.size(); i++){
        if()
    }
}