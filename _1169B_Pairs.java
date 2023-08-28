package codeforcesJavaProject;

import java.util.*;

public class _1169B_Pairs  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int upper_bound = scanner.nextInt();
        int pairCount = scanner.nextInt();

        ArrayList<KeyboardPair> pairs = new ArrayList<>();
        for (int i = 0; i < pairCount; i++) {
            int keyA = scanner.nextInt();
            int keyB = scanner.nextInt();
            pairs.add(new KeyboardPair(keyA, keyB));
        }

        if (isPossible(upper_bound, pairs)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    private static boolean isPossible(int upper_bound, ArrayList<KeyboardPair> pairs) {
        KeyboardPair firstPair = pairs.get(0);

        for (int num : new int[] {firstPair.keyA, firstPair.keyB}) {
            int[] voteCounts = new int[upper_bound + 1];
            int countWithoutNum = 0;

            for (KeyboardPair pair : pairs) {
                if (pair.keyA != num && pair.keyB != num) {
                    voteCounts[pair.keyA]++;
                    voteCounts[pair.keyB]++;
                    countWithoutNum++;
                }
            }

            if (getMaxVoteCount(voteCounts) == countWithoutNum) {
                return true;
            }
        }

        return false;
    }

    private static int getMaxVoteCount(int[] voteCounts) {
        int max = voteCounts[0];
        for (int i = 1; i < voteCounts.length; i++) {
            max = Math.max(voteCounts[i], max);
        }
        return max;
    }

    static class KeyboardPair {
        int keyA;
        int keyB;

        KeyboardPair(int a, int b) {
            keyA = a;
            keyB = b;
        }
    }
}
