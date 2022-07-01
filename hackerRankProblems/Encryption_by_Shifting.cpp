#include <iostream>
#include <vector>
// #include <bits/stdc++.h>;
using namespace std;

char checkValid(int val){
    if(val >= 65 && val <= 90){
        return char(val);
    }else if(val <0){
        return char(91 + val);
    }{
        return char(val+65);
    }
}


int main(){
    char cipher[] = "SGZVQBUQAFRWSLC";
    char key[] = "ACM";
    // cin >> cipher >> key;
    // cout << "hello\n";
    // length to decrypt message
    int length = sizeof(cipher) / sizeof(cipher[0]);
    int start = sizeof(key) / sizeof(key[0]);
    // index at start of key
    int keyIndex = 0;
    // append the key to front of cipher
    vector<char> messageToDecrypt;
    // cout << start<<endl;
    for (int i=0; i<start-1; i++){
        messageToDecrypt.push_back(key[i]);
    }
    for (int i=0; i<length-1; i++){
        messageToDecrypt.push_back(cipher[i]);
    }
    for (int i=0; i< messageToDecrypt.size(); i++) cout << messageToDecrypt[i];
    
    cout << endl;
    
    for (int i=start-1; i<length-1; i++){
        if(keyIndex >= start-1){
            int newIndex = keyIndex%start-1;
            cout << newIndex << endl;
            // newIndex += keyIndex;
            cout <<messageToDecrypt[i] <<" "<< messageToDecrypt[keyIndex] <<"\n";
            cout << checkValid( (messageToDecrypt[i]) - (messageToDecrypt[keyIndex] - messageToDecrypt[newIndex-2]) )<< endl;
            keyIndex++;
            continue;
        }
        cout <<messageToDecrypt[i] <<" "<< messageToDecrypt[keyIndex] <<"\n";
        cout << checkValid( (messageToDecrypt[i]) - (messageToDecrypt[keyIndex]) )<< endl;
        keyIndex++;
    }
    cout << "\n";
    return 0;
}