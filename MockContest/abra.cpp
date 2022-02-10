#include <iostream>
using namespace std;

int main(){
    int input, stop=1;
    string abra="Abracadabra";
    cin >> input;
    while(true){
        if(stop > input){
            break;
        }
        cout << stop << " "<<  abra<< endl;
        stop++;
    }
    return 0;
}