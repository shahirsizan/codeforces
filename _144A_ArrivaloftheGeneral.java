package codeforcesJavaProject;
import java.util.Scanner;

public class _144A_ArrivaloftheGeneral {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        int[] heights = new int[n];

        for (int i = 0; i < n; i++) {
            heights[i] = scanner.nextInt();
        }

        int maxHeight = heights[0];
        int minHeight = heights[0];
        int maxIndex = 0;
        int minIndex = 0;

        for (int i = 1; i < n; i++) {
            if (heights[i] > maxHeight) {
                maxHeight = heights[i];
                maxIndex = i;
            }
            if (heights[i] <= minHeight) {
                minHeight = heights[i];
                minIndex = i;
            }
        }

        int seconds = maxIndex + (n - 1 - minIndex);
        if (maxIndex > minIndex) {
            seconds--;
        }

        System.out.println(seconds);
        scanner.close();
    }
}
