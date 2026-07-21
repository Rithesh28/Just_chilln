package number_programming;
import java.util.Scanner;
public class automorphicnumber {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int n=sc.nextInt();
        int temp1=n;
        int square=temp1*temp1;
        int count=0;
        while(temp1>0){
            //int d=n%10;
            count++;
            temp1/=10;
        }
       int divisor=1;
       int temp=square;
        for(int i=0;i<count;i++){
            divisor*=10;
            
        }
        temp=temp%divisor;
        if(temp==n){
            System.out.println("Automorphic number");
        }
        else{
            System.out.println("Not an Automorphic number");
        }
    }
}