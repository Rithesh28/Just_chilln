import java.util.Scanner;

public class countwords {
     public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int words=0;
        int spaces=0;
        System.out.println("Enter a string:");
        String s=sc.nextLine();
        for(int i=0;i<=s.length();i++){
            char ch=s.charAt(i);
            words=spaces+words;
            
        }
        System.out.println(words);
        
    }
}
