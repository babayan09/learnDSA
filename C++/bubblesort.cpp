#include <iostream>
using namespace std;

int main(){
int size;
    int arr[100];
    cout<<"Enter the Number of elements you want to store \n";
    cin>>size;
     cout<<"Enter the Number of elements \n ";
   for(int i =0;i<size;i++)
    {
        cin>>arr[i];
    }

    

    for(int i=1; i<size; i++){

        for(int j=0;j<size-1;j++){
            if(arr[j]>arr[j+1]){
                int temp;

               temp= arr[j];
               arr[j]=arr[j+1];
               arr[j+1]=temp;

    }

            }

    }
            for(int i=0;i<size;i++){
        cout<<arr[i];
        cout<<" ";
         }

    }

