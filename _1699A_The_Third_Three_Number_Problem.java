package codeforcesJavaProject;

import java.util.Scanner;

public class _1699A_The_Third_Three_Number_Problem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            if (n % 2 == 1) {
                System.out.println(-1);
            } else {
                System.out.println(n/2 + " " + 0 + " " + 0);
            }
        }
        scanner.close();
    }
}

