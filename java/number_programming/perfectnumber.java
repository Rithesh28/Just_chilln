package number_programming;
import java.util.Scanner;
public class perfectnumber {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter a number:");
        int n=sc.nextInt();
        int temp=n;
        int sum=0;
        for(int i=1;i<=temp-1;i++){
            if(temp%i==0){
                sum=sum+i;
            }

        }
        if(n==sum){
            System.out.println("perfect no");
        }
        else{
            System.out.println("Not perfect");
        }
    }
}
