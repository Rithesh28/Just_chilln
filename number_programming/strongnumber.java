package number_programming;
import java.util.Scanner;
public class strongnumber {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int n=sc.nextInt();
        int temp=n;
        
        int sum=0;
        while(temp>0){
            int fact=1;
            int digit=temp%10;
            for(int i=1;i<=digit;i++){
                fact=fact*i;
            }
            sum=sum+fact;
            temp/=10;
        }
        if(n==sum){
            System.out.println("Strong number");
        }
        else{
            System.out.println("Not strong");
        }
    }
}
