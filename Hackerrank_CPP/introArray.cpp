#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
using namespace std;
int main() 
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
{
    int n;
    cin>>n;
    int arr[n];
    for(int x=0;x<n;x++)
    {
        cin>>arr[x];
    }   
    for(int x=0;x<n;x++)
    {
        cout<<arr[n-x-1]<<' ';
    }
    return 0;
}
