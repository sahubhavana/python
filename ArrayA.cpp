#include<iostream>
using namespace std;
int main(){
int n,sum=0;
scanf("%d",&n);
int a[100];
for(int i=0;i<n;i++){
    scanf("%d",&a[i]);
}
for(int i=0;i<n;i++){
    sum=sum+a[i];
}
printf("%d",sum);
}