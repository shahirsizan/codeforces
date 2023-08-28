package codeforcesJavaProject;

import java.util.Scanner;

public class _1335B_Construct_the_String  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();

            for (int i = 0; i < n; i++) {
                char ch = (char) ('a' + i % b);
                System.out.print(ch);
            }
            System.out.println();
        }
        sc.close();
    }
}
