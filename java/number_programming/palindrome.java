package number_programming;
import java.util.Scanner;
public class palindrome {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int n=sc.nextInt();
        int temp=n;
        int rev=0;
        while(temp>0){
            int digit=temp%10;
            rev=rev*10+digit;
            temp/=10;
        }
        //System.out.println(rev);
        if(n==rev){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not");
        }
    }
    
}
