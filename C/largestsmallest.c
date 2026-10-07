#include<stdio.h>
#include<stdlib.h>
int main(){
    int n;
    
    printf("Enter the number:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array numbers:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int largest=arr[0];
    int smallest=arr[0];
    for(int i=0;i<n;i++){
    
    if(arr[i]>=largest){
        largest=arr[i];

    }
    if(arr[i]<=smallest){
        smallest=arr[i];
    }
    }
    printf("%d\n", smallest);
    printf("%d\n", largest);
    return 0;

}