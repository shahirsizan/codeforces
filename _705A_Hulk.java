package codeforcesJavaProject;

import java.util.Scanner;

public class _705A_Hulk{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        StringBuilder feeling = new StringBuilder("I hate");

        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                feeling.append(" that I love");
            } else {
                feeling.append(" that I hate");
            }
        }

        feeling.append(" it");
        System.out.println(feeling.toString());
    }
}
