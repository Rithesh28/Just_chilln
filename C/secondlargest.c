#include<stdio.h>
int main(){
    int n;
    printf("Enter the number:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array numbers:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    int second=arr[0];
    for(int i=0;i<n;i++){
        if(arr[i]>max){
            second=max;
            max=arr[i];
        }
        else if(arr[i]>second){
            second=arr[i];
        }
    }
    printf("%d",second);
    return 0;
}
