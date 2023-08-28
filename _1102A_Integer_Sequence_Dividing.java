package codeforcesJavaProject;

import java.util.*;

public class _1102A_Integer_Sequence_Dividing  {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(findMinimumDifference(scanner.nextLong()));
    }

    public static int findMinimumDifference(long n){
        return (n * (n+1)/2) % 2 == 0 ? 0 : 1;
    }
}
