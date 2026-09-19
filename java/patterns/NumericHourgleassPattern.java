import java.util.Scanner;

public class NumericHourgleassPattern {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N Value: ");
        int n = sc.nextInt();

        // Upper half (rows with decreasing elements)
        for (int i = n; i >= 1; i--) {
            // Leading spaces for alignment
            for (int s = 0; s < (n - i) * 2; s++) {
                System.out.print(" ");
            }
            int count = 2 * i - 1;
            for (int j = 1; j <= count; j++) {
                System.out.print(j + (j == count ? "" : " "));
            }
            System.out.println();
        }

        // Lower half (rows with increasing elements)
        for (int i = 2; i <= n; i++) {
            // Leading spaces for alignment
            for (int s = 0; s < (n - i) * 2; s++) {
                System.out.print(" ");
            }
            int count = 2 * i - 1;
            for (int j = 1; j <= count; j++) {
                System.out.print(j + (j == count ? "" : " "));
            }
            System.out.println();
        }

        sc.close();
    }
}