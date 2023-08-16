package codeforcesJavaProject;

import java.util.*;

public class _1807B_Grab_the_Candies {
	
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        while (t-- > 0) {
        	
            int n = scanner.nextInt();
            int mihaiCandies = 0;
            int biancaCandies = 0;
            
            for (int i = 0; i < n; i++) {
                int candies = scanner.nextInt();
                
                if (candies % 2 == 0) {
                    mihaiCandies += candies;
                } else {
                    biancaCandies += candies;
                }
            }
            
            if (mihaiCandies > biancaCandies) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        scanner.close();
    }
}
