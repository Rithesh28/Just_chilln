package number_programming;
import java.util.Scanner;
public class primeinrange {
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the first number:");
        int start=sc.nextInt();
        System.out.println("Enter the last number:");
        int end=sc.nextInt();
        for(int i=start;i<=end;i++){
            int current=i;
            if(current<=1){
                continue;
            }
            boolean isprime=true;
            for(int j=2;j<=current-1;j++){
                if(current%j==0){
                    isprime=false;
                    break;
                }
            }
                if(isprime){
                System.out.println(current);
            }
        }
    }
}
