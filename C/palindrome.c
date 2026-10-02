#include<stdio.h>
#include<stdlib.h>
int main(){
    int n, rev=0;
    printf("Enter the number:");
    scanf("%d",&n);
    int temp=n;
    while(temp!=0){
        int digit=temp%10;
        rev=rev*10+digit;
        temp/=10;
    }
    if(n==rev){
        printf("Palindrome");
    }
    else{
        printf("Not palindrome");
    }
    return 0;

}