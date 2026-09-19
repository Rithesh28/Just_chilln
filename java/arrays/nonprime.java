package arrays;
import java.util.Scanner;
public class nonprime {
    // Check whether a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        // Remove braces, parentheses, and brackets
        input = input.replaceAll("[{}\\[\\]()]", "").trim();

        // Split numbers separated by commas or spaces
        String[] tokens = input.split("[,\\s]+");

        StringBuilder result = new StringBuilder();
        for (String token : tokens) {
            if (!token.isEmpty()) {
                int num = Integer.parseInt(token.trim());
                if (!isPrime(num)) {
                    if (result.length() > 0) {
                        result.append(",");
                    }
                    result.append(num);
                }
            }
        }

        System.out.println(result);
        sc.close();
    }
}
