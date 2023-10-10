#include<stdio.h>
int solution(int N)
{
    //write your code here
    int wt[N],p[N];
    float p_per_unit[N];
    for(int i= 0;i<N;i++){
        scanf("%d",&wt[i]);
    }
    for(int i=0;i<N;i++)
              scanf("%d",&p[i]);   
    int knapsack;
    scanf("%d",&knapsack);
    for(int i=0;i<N;i++)
              p_per_unit[i] =(float)(p[i])/(float)(wt[i]);
    int i=0,j=0;
    for(int i=0;i<N;i++){
    for(int j=0;j<N-i-1;j++){
    if(p_per_unit[j] <p_per_unit[j+1]){
    float temp = p_per_unit[j];
        p_per_unit[j] =p_per_unit[j+1];
        p_per_unit[j+1] =temp;
    int tempo=wt[j];
        wt[j] = wt[j+1];
        wt[j+1] =tempo;
        tempo= p[j];
        p[j]= p[j+1];
        p[j+1]=tempo;
    }
    } 
    }
    int profit=0;
    i=0;
    while(knapsack){
        if (knapsack >=wt[i]&&wt[i]!=0){
            knapsack -=wt[i];
            wt[i] =0;
            profit+=p[i];
        }
        if (knapsack<wt[i]){
            profit+=knapsack*p_per_unit[i];
            knapsack=0;
            break;
        }
        i++;
    }
    printf("%d",profit);
}

int main()
{
    int N;
    scanf("%d",&N);
   solution(N);
}