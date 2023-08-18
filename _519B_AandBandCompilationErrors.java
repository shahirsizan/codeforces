package codeforcesJavaProject;

import java.util.Scanner;

public class _519B_AandBandCompilationErrors {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        long sumA = 0, sumB = 0, sumC = 0;

        for (int i = 0; i < n; i++){
            sumA += scanner.nextLong();
        }

        for (int i = 0; i < n - 1; i++){
            sumB += scanner.nextLong();
        }

        System.out.println(sumA - sumB);

        for (int i = 0; i < n - 2; i++){
            sumC += scanner.nextLong();
        }

        System.out.println(sumB - sumC);
        scanner.close();
    }

}