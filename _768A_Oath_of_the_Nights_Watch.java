package codeforcesJavaProject;

import java.util.*;

public class _768A_Oath_of_the_Nights_Watch  {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        int[] stewards = new int[n];
        for (int i = 0; i < n; i++) {
            stewards[i] = scanner.nextInt();
        }

        Arrays.sort(stewards);

        int count = 0;
        for (int i = 1; i < n-1; i++) {
            if (stewards[i] > stewards[0] && stewards[i] < stewards[n-1]) {
                count++;
            }
        }

        System.out.println(count);
        scanner.close();
    }
}
