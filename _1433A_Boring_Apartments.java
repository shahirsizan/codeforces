package codeforcesJavaProject;

import java.util.*;

public class _1433A_Boring_Apartments {
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        while (t-- > 0) {
        	
            int who_answered = scanner.nextInt();
            int who_answered_last_digit = who_answered % 10; 
            int digitsPressed = 0;

            digitsPressed += (who_answered_last_digit - 1) * 10;
            
            
            while(true) {
            	digitsPressed += String.valueOf(who_answered).length();
            	who_answered = who_answered / 10;
            	if(who_answered == 0) {
            		break;
            	}
            }

            System.out.println(digitsPressed);
        }
        scanner.close();
    }
}

