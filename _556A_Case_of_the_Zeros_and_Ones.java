package codeforcesJavaProject;

import java.util.Scanner;

public class _556A_Case_of_the_Zeros_and_Ones  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = sc.next();

        int ones = 0;
        int zeros = 0;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '1') {
                ones++;
            } else {
                zeros++;
            }
        }

        System.out.println(Math.abs(ones - zeros));

        sc.close();
    }
}
