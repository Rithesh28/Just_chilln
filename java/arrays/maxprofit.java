package arrays;
import java.util.Scanner;
public class maxprofit{
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of array:");
        int n=sc.nextInt();
        System.out.println("Enter the array:");
        int prices[]=new int[n];
        for(int i=0;i<=prices.length-1;i++){
            prices[i]=sc.nextInt();
        }
        int min=prices[0];
        int max=prices[0];
        for(int i=0;i<=prices.length-1;i++){
            if(min<=prices[i]){
                min=prices[i];
            }
        }
        for(int i=0;i<=prices.length-1;i++){
            if(max>=prices[i]){
                max=prices[i];
            }
        }
        int profit=max-min;
        System.out.println(profit);
    }
}