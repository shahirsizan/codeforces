package codeforcesJavaProject;

import java.util.Scanner;

public class _1360A_Minimal_Square {
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        while (t-- > 0) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            
            int side = Math.max(2 * Math.min(a, b), Math.max(a, b));
            int area = side * side;
            
            System.out.println(area);
        }
        
        scanner.close();
    }
}
