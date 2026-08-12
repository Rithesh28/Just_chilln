import java.util.Scanner;
public class reversepali {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        char ch;
        String temp="";
        System.out.println("Enter a string:");
        String s=sc.nextLine();
        for(int i=s.length()-1;i>=0;i--){
            ch=s.charAt(i);
            temp=temp+ch;
            //System.out.print(ch);
        }
        if(s.equals(temp)){
            System.out.println("Palindrome");
        }
        else{
            System.out.println("Not a palindrome");
        }
        
    }
    
}

