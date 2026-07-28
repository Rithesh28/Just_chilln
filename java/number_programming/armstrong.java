package number_programming;
import java.util.Scanner;
public class armstrong {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int n=sc.nextInt();
        int temp=n;
        int count=0;
        while(temp>0){
            int digit=temp%10;
            count++;
            temp/=10;
        }
        int temp1=n;
        
        int sum=0;
        while(temp1>0){
            int digit=temp1%10;
            int cube=1;
            for(int i=0;i<count;i++){
                cube=cube*digit;
            }
            sum=sum+cube;
            temp1/=10;
        }
        if(n==sum){
            System.out.println("Armstrong Number");
        }
        else{
            System.out.println("Not an Armstrong");
        }
    }
}
