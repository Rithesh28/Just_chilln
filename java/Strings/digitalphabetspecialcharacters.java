import java.util.Scanner;
public class digitalphabetspecialcharacters{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the string:");
        String s=sc.nextLine();
        //int vowels=0;
        int alphabets=0;
        int digits=0;
        int special=0;
        for(int i=0;i<=s.length()-1;i++){
            char ch=s.charAt(i);
            if((ch>=97 && ch<=122) || (ch>=65 && ch<=90)) {
                alphabets++;
            }
            else if(ch>=48 && ch<=57){
                digits++;
            }
            else if(ch>=33 && ch<=126){
                special++;
            }
        }
        //System.out.println("Vowels:" +vowels);
        System.out.println("Alphabets:" +alphabets);
        System.out.println("Digits:" +digits);
        System.out.println("Special:" +special);
    }
}