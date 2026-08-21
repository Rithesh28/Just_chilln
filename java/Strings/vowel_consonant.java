import java.util.Scanner;
public class vowel_consonant{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the string:");
        String s=sc.nextLine();
        int vowels=0;
        int consonant=0;
        for(int i=0;i<=s.length()-1;i++){
            char ch=s.charAt(i);
            if((ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') && (ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U')){
                vowels++;
            }
            else {
            consonant++;
            }
        }
        System.out.println("Vowels:" +vowels);
        System.out.println("Consonants:" +consonant);
        
    }
}