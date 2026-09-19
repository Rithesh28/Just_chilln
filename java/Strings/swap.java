import java.util.Scanner;

public class swap{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter String 1: ");
        String str1 = sc.nextLine();
        
        System.out.print("Enter String 2: ");
        String str2 = sc.nextLine();

        str1 = str1 + str2;
        str2 = str1.substring(0, str1.length() - str2.length());
        str1 = str1.substring(str2.length());

        System.out.println("\nAfter Swapping:");
        System.out.println("String 1: " + str1);
        System.out.println("String 2: " + str2);
        
        sc.close();
    }
}