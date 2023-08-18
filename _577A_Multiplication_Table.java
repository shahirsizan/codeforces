package codeforcesJavaProject;

import java.util.Scanner;

public class _577A_Multiplication_Table {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = sc.nextInt();
        int count = 0;

        for (int i = 1; i <= n; i++) {
            int div = x / i;
            if (div >= 1 && div <= n && div*i == x) {
                count++;
            }
        }
        System.out.println(count);
    }
}
