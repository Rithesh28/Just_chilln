#include<stdio.h>
int main(){
    int n;
    int found=0;
    printf("Enter the number:");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array numbers:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    int max=arr[0];
    int second=0;
    for(int i=0;i<n;i++){
        if(arr[i]>max){
            second=max;
            max=arr[i];
            found=1;
        }
        else if(arr[i]<max){
            if(found==0 || arr[i]>second){
                second=arr[i];
                found=1;
            }
        }
    
    }
    if(found==1){
        printf("Possible\n");
    }
    else{
        printf("Not Possible\n");
    }
    printf("%d\n",second);
    return 0;
}
