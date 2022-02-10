#include <iostream>
using namespace std;

int main(){
    int input, stop=0;
    string abra="Abracadabra";
    cin >> input;
    while(true){
        if(stop == input){
            break;
        }
        cout << abra;
        stop++;
    }
}