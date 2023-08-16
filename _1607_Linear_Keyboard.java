package codeforcesJavaProject;

import java.util.Scanner;

public class _1607_Linear_Keyboard {
	
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        
        while (testCases-- > 0) {
        	
            String keyboardLayout = scanner.next();
            String targetWord = scanner.next();
            int totalTime = 0;
            
            for (int i = 1; i < targetWord.length(); i++) {
                int prevCharIndex = keyboardLayout.indexOf(targetWord.charAt(i - 1));
                int currCharIndex = keyboardLayout.indexOf(targetWord.charAt(i));
                totalTime += Math.abs(prevCharIndex - currCharIndex);
            }
            
            System.out.println(totalTime);
        }
        scanner.close();
    }
}
