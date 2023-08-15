package codeforcesJavaProject;

import java.util.Arrays;
import java.util.Scanner;

public class _758A_Holiday_Of_Equality{
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        int[] citizens_welfare_list = new int[n];
        
        for (int i=0; i<n; i++) {
            citizens_welfare_list[i] = scanner.nextInt();
        }
        
        int maxWealth = Arrays.stream(citizens_welfare_list).max().getAsInt();
        // int maxWealth = Math.max(citizens_welfare_list);
        // THIS LINE RENDERS ERROR
        int totalExpenses = 0;
        
        for (int wealth : citizens_welfare_list) {
            totalExpenses += maxWealth - wealth;
        }
        
        scanner.close();
        System.out.println(totalExpenses);
    }
}


