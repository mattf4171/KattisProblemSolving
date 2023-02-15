/*
 * Title: BFSTraversal.cpp
 * Abstract: Program that conducts the BFS traversal of a graph and displays city names 
			 in the range of hop(s) from a starting city.
 * Name: Matthew Fernandez
 * Date: 2/14/2023
 */

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void BFS(vector<vector<int>> g, vector<vector<int>> & mark, int total_hops, int start){
	queue<int> q;
	mark[start][1] =0; // mark starting node as 0
	q.push(mark[start][0]);

	while(!q.empty()){
		int curr = q.front();
		q.pop();
		for(int j=0; j< g.size(); j++){
			if(g[curr][j] == 1 && mark[j][1] == -1){
				mark[j][1] = mark[curr][1]+1;
				q.push(j);
			}
		}
	}
}

int main()
{
	// most of the main Fn was recycled from main_hw5_2.cpp
	int numVertices, edges, starter=0, start_vertex, total_hops;
	string vertName, start_node_string;
	vector<vector<int>> vertices; // 2d vector
	unordered_map<int, string> intToStringMap; // hashing is faster
	unordered_map<string, int> stringToIntMap;
	map<string, int> mark2; // create mark array initialized with -1 should be a map with string, int
	vector<vector<int>> mark;
	cin >> numVertices;
	while(numVertices--){
		cin >> vertName;
		intToStringMap.insert(pair<int,string>( starter, vertName )); // will use to display proper vertices
		stringToIntMap.insert(pair<string,int>( vertName, starter));
		mark2.insert(pair<string, int> (vertName, -1));
		vector<int> tempMark;
		tempMark.insert(tempMark.end(), {starter, -1});
		mark.push_back(tempMark);
		starter+=1;
	}

	for (int i=0; i<stringToIntMap.size();i++)
    {
		vector<int> v;
        for (int j=0; j<stringToIntMap.size(); j++)
        {
            v.push_back(0);
        }   
		vertices.push_back(v);
    }
	cin >> edges;
	string startStrEdge, endStrEdge;
	int startIntEdge, endIntEdge, cost, totalCost;
	while(edges--){
		cin >> startStrEdge >> endStrEdge;
		auto it = stringToIntMap.find(startStrEdge);
		if(it != stringToIntMap.end()){
			// Key found
			startIntEdge = it->second;
		}

		auto it2 = stringToIntMap.find(endStrEdge);
		if(it2 != stringToIntMap.end()){
			// key found
			endIntEdge = it2->second;
			// cout << "endEdge -> " << endIntEdge << endl;
		}
		
		vertices[startIntEdge][endIntEdge] = 1;
	}
	cin >> start_node_string;
	auto sNode = stringToIntMap.find(start_node_string);
	if(sNode != stringToIntMap.end()){
		start_vertex = sNode->second;
	}
	cin >> total_hops;
	BFS(vertices, mark, total_hops, start_vertex); // BFS Fn

	// apply changes to mark2 with updated mark array
	for(int i=0; i< mark.size(); i++){
		for(auto mapIterator = intToStringMap.begin(); mapIterator != intToStringMap.end(); mapIterator++ ){ // uses the key/value of the unordered map to get the appropriate mark array into the mark2 array that will be used for ouput purposes
			if(mark[i][0] == mapIterator->first){
				auto it = mark2.find(mapIterator->second);
				if(it != mark2.end()){
					mark2.erase(it);
					mark2.insert(pair<string,int> (mapIterator->second, mark[i][1]));
				}
			}
		}
	}
	// show the mark array
	for(auto it = mark2.begin(); it != mark2.end(); it++){
		if(it->second != -1 && it->second <= total_hops ){
			cout << it->first << ":" << it->second << endl;	
		}
	}	
	return 0;
}

// Input:
// 5
// Fresno
// LA
// SD
// SF
// NYC
// 6
// SD LA
// SD NYC
// LA NYC
// SF Fresno
// SF SD
// Fresno SD
// SF
// 2

/*
Output:
Fresno:1
LA:2
NYC:2
SD:1
SF:0
*/
