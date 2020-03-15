#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a,b;
    cin>>a>>b;
    cout<<a.length()<<' '<<b.length();
    cout<<'\n'<<a+b<<'\n';
    char ch=a.at(0);
    char c= b.at(0);
    a=c+a.substr(1);
    b=ch+b.substr(1);
    cout<<a<<' '<<b;
    return 0;
}