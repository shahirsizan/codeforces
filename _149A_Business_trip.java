package codeforcesJavaProject;

import java.util.*;

public class _149A_Business_trip {
	
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int k = scanner.nextInt();
        
        int[] growthRates = new int[12];
        Arrays.setAll(growthRates, i -> scanner.nextInt());
        Arrays.sort(growthRates);
        
        int months = 0;
        int totalGrowth = 0;

        for (int i = 11; i >= 0; i--) {
            if (totalGrowth >= k) {
                break;
            }
            totalGrowth += growthRates[i];
            months++;
        }

        if (totalGrowth < k) {
            System.out.println(-1);
        } else {
            System.out.println(months);
        }

        scanner.close();
    }
}
