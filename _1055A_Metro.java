package codeforcesJavaProject;

import java.util.Scanner;

public class _1055A_Metro {
	
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); 
        int s = scanner.nextInt();
        
        int[] firstTrack = new int[n + 1];
        int[] secondTrack = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            firstTrack[i] = scanner.nextInt();
        }

        for (int i = 1; i <= n; i++) {
            secondTrack[i] = scanner.nextInt();
        }

        
        if (firstTrack[1] == 0) {				// Bob simply can't enter the metro system
            System.out.println("NO"); 
        } 
        else if (firstTrack[1] == 1 && firstTrack[s] == 1) {
            System.out.println("YES");		// Bob can easily visit Alice by using the firstTrack
            
        } 
        												// Bob would need to use the first track and then the second track
        else if (firstTrack[1] == 1 && firstTrack[s] == 0 && secondTrack[s] == 1) {
        	
            for (int i = s+1; i <= n; i++) {
            	
                if (firstTrack[i] == 1 && secondTrack[i] == 1) {
                    System.out.println("YES");
                    return;
                }
            }
            System.out.println("NO");
        } 
        else {
            System.out.println("NO");
        }
        scanner.close();
    }
}
