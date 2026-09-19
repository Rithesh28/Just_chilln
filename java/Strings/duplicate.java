import java.util.Scanner;

public class duplicate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine().toLowerCase();

        // Track already processed characters to avoid printing duplicates
        boolean[] visited = new boolean[str.length()];

        // Find and collect all repeating characters in order of appearance
        StringBuilder repeatingList = new StringBuilder();
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (ch == ' ' || visited[i]) continue;

            int count = 0;
            for (int j = i; j < str.length(); j++) {
                if (str.charAt(j) == ch) {
                    count++;
                }
            }

            if (count > 1) {
                if (repeatingList.length() > 0) {
                    repeatingList.append(",");
                }
                repeatingList.append(ch);
            }
        }

        System.out.println("Repeating Letters: " + repeatingList);

        // Find and print 1-based positions for each repeating character
        String[] repChars = repeatingList.toString().split(",");
        for (String rc : repChars) {
            if (rc.isEmpty()) continue;
            char target = rc.charAt(0);

            StringBuilder positions = new StringBuilder();
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == target) {
                    if (positions.length() > 0) {
                        positions.append(",");
                    }
                    positions.append(i + 1); // 1-based index
                }
            }
            System.out.println("Position of '" + target + "': " + positions);
        }

        sc.close();
    }
}