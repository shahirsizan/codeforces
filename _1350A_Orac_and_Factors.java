package codeforcesJavaProject;

import java.util.Scanner;

public class _1350A_Orac_and_Factors {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int k = scanner.nextInt();

            int smallestDivisor = smallestDivisor(n);
            int result = n + smallestDivisor + 2 * (k - 1);

            System.out.println(result);
        }
        scanner.close();
    }

    static int smallestDivisor(int n) {
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return n;
    }
}
