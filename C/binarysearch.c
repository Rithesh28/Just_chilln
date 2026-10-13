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
    int low=0;
    int high=n-1;
    int mid;
    while(low<=high){
        mid=(low+high)/2;
        if(arr[mid]==ele){
            printf("%d",mid);
            found=1;
            break;
        }
        else if (ele<arr[mid]){
            high=mid-1;
        }
        else{
            low=mid+1;
        }
    }
    if(found==0){
        printf("-1\n");
    }
    return 0;
}