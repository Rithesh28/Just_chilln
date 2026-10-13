#include<stdio.h>
int main(){
    int n;
    int total;
    printf("Enter the number:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array numbers:\n");
    for(int i=0;i<n-1;i++){
        scanf("%d",&arr[i]);
    }
    total=n*(n+1)/2;
    //printf("%d",total);
    int missing=total;
    for(int i=0;i<n-1;i++){
        missing=missing-arr[i];

    }
    printf("%d",missing);
    return 0;
}