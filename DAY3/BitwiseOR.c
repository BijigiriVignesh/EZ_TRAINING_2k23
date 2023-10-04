
#include <stdio.h>
int main(){
    int a =10;
    if(a>100 | a++<200 | a++ == 12) // executes all the statements irrespective of either true or false
        //the result is same as logical OR but the entire statements are executed.

    printf("hello %d",a);
    else
    printf("hai %d",a);
}