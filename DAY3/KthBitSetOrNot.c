#include <stdio.h>
/*
check if the kth bit from the right is set or not.
*/
int main(){
	long int a =14 , c=0,k=3;
	long int res[100],j=0;
	while(a>=2){
		res[j++] =a%2;
		a /=2;		
	}
	res[j] = a;
	if(res[k])
	printf("Set");
	else
	printf("Not Set");
	return 0;
}
/*
Other method is 
if(a & (1 << (i-1)))
printf("Set");
else
printf("Not Set");
*/