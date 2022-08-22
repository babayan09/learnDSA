#include <iostream>
using namespace std;
int main(){

int size,element,pos;
    int arr[10];
    cout<<"Enter the Number of elements you want to store \n";
    cin>>size;
     cout<<"Enter the Number of elements \n ";
   for(int i =0;i<size;i++)
    {
        cin>>arr[i];
    }
cout<<"Enter Number to INSERT ARRAY AND POSTION INTO \n";
cin>>pos;
cout<<"Enter Number  POSTION INTO \n";
cin>>element;

    for(int i=size; i>=element;i--){
        arr[i+1]=arr[i];
    
    }
    arr[element]=pos;
    cout<<"Elements After Insertion \n";
    for(int i=0;i<=size+1;i++){
        cout<<arr[i]<<" ";
        cout<<endl;

    }

    return 0;

}