#include <iostream>
using namespace std;

int factorial(int num){
int fact=1;
       for(int i=1;i<=num;i++){
           fact*=i;
           }
        return fact;

    }
int main(){

    int n;
    int r;

    cout<<"Enter n=> \n";   
     cin>>n;
    cout<<"Enter r => \n";
    cin>>r;

int ncr=factorial(n)/(factorial(n-r)*factorial(r));

cout<<"nCr is "<<ncr;


    return 0;
}