#include<stdio.h>
int main(){
    int n;
    int ele;
    int found=0;
    printf("Enter the number:\n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter the array elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter the search element:\n");
    scanf("%d",&ele);
    for(int i=0;i<n;i++){
        if(ele==arr[i]){
            printf("%d",i);
            found=1;
            break;
        }
    }
    if(found==0){
        printf("the entered element is not present in the array");
    }
    return 0;
}