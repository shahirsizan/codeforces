package codeforcesJavaProject;

import java.util.Scanner;

public class _1367B_Even_Array {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int testcase = 0; testcase < t; testcase++) {
            int n = scanner.nextInt();
            
            // Initialize `evens` and `odds` to keep track of the number of 
            // odd-indexes and even-indexes both having odd numbers.
            int odds = 0, evens = 0;
            
            for (int i = 0; i < n; i++) {
                int num = scanner.nextInt();
                if (i%2 != num%2) {
                    if (i % 2 == 0) {
                        evens++;
                    } else {
                        odds++;
                    }
                }
            }
            
            if (odds != evens) {
                System.out.println(-1);
            } else {
                System.out.println(odds);
            }
        }
        
        scanner.close();
    }
}

