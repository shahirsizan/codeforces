package codeforcesJavaProject;

import java.util.*;

public class _1041A_Heist  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        Arrays.sort(a);
        int count = a[n-1] - a[0] + 1 - n;
        // 10 13 12 8
        // After sorting
        // 8 10 12 13
        // `a[n-1] - a[0] + 1` will find the number of keyboards in the
        // range 8 -> 13(inclusive) = 6. Now as remaining keyboard count is n=4
        // So, minimum possible lost count is = 6-4 = 2

        System.out.println(count);
        scanner.close();
    }
}
