package codeforcesJavaProject;

import java.util.Scanner;

public class _1370A_Maximum_GCD {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
            int n = scanner.nextInt();
            int maxGCD = n / 2;
            //Since the GCD of two integers cannot exceed half of their sum, the maximum possible GCD is n / 2.
            System.out.println(maxGCD);
        }
    }
}

