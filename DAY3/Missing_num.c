#include <stdio.h>
int main(){
/*
find the missing number in the array

*/
    int a[] = {1,2,3,4,5,6,7,9};
    int x = 0, i=0;
    for (int i = 0;i<=8;i++)
    x ^= i;
    for(int i=0;i<8-1;i++)
    x^= a[i];
    printf("%d",x);
}