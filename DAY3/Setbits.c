#include <stdio.h>
int main(){
	long int a =15;
	if (a <0)a *= -1;
	long int c=0;
	while(a>=2){//Binary conversion of a.
		if(a%2)c++;// checking if the bit was set or not.
		a = a/2;
	}
	if(a)c++;
	printf("%ld",c);
}