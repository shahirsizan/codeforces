package codeforcesJavaProject;

import java.util.*;

public class _1624A_Plus_One_on_the_Subset{
	
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        while (t-- > 0) {
            int n = scanner.nextInt();
            int[] a = new int[n];
            
            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextInt();
            }
            
            Arrays.sort(a);
            int min_operation_needed = a[n - 1] - a[0];
            
            System.out.println(min_operation_needed);
        }
        
        scanner.close();
    }
}


