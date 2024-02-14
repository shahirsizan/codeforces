package codeforcesJavaProject;

import java.util.*;

public class _1385B_Restore_the_Permutation_by_Merger  {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int[] permutationList = new int[2 * n];

            for (int j = 0; j < 2*n; j++) {
                permutationList[j] = sc.nextInt();
            }

            HashSet<Integer> sett = new HashSet<>();
            for (int num : permutationList) {
                if (!sett.contains(num)) {
                    System.out.print(num + " ");
                    sett.add(num);
                }
            }
            System.out.println();
        }
        sc.close();
    }
}
