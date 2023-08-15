package codeforcesJavaProject;

import java.util.Scanner;

public class _339B_Xenia_and_Ringroad {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        
        int[] tasks = new int[m];
        for (int i=0; i<m; i++) {
            tasks[i] = scanner.nextInt();
        }
        
        int currentPosition = 1;
        long timeNeeded = 0;
        
        for (int task : tasks) {
            if (task >= currentPosition) {
                timeNeeded += task - currentPosition;
            } 
            else {
                timeNeeded += n - currentPosition + task;
            }
            currentPosition = task;
        }
        scanner.close();
        System.out.println(timeNeeded);
    }
}