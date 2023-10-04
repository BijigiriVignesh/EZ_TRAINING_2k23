#include <stdio.h>
/*
check if the kth bit from the right is set or not.
*/
int main(){
	long int a = -15 , c=0;
	while(a>=2){
		if(a%2)c++;
		if (c>1)break;
		a /=2;		
	}
	if (c ==1)
	printf("Yes");
	else
	printf("No");
	
}