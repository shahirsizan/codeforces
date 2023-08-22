package codeforcesJavaProject;

import java.util.*;

public class _1850A_To_My_Critics {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int length = 3;

            int[] digits = {a, b, c};
            Arrays.sort(digits);

            if (digits[length-1] + digits[length-2] >= 10) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
