#include <stdio.h>
int main(){
    int a =12;
    if(a&1)//Checking if the LSB bit is set or not.
    
    {
        printf("Odd number");//Odd numbers have the LSB as 1.
    }
    else{
        printf("Even number");
    }
}