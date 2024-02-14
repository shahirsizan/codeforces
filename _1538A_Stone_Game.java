package codeforcesJavaProject;

import java.util.Arrays;
import java.util.Scanner;

public class _1538A_Stone_Game {
    
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();
        
        while (testCases-- > 0) {
        	
            int fromLeftLow = 0, fromLeftHigh = 0;
            
            int[] arr = new int[scanner.nextInt()];		// INITIALIZE THE ARRAY
            Arrays.setAll(arr, i -> scanner.nextInt());	// DEFINE THE ARRAY
            
            //	Sort the cloned array temp to find the minimum and maximum values.
            int[] temp = arr.clone();
            Arrays.sort(temp);
            int min = temp[0];
            int max = temp[temp.length - 1];
            
            //	Loop through the original array arr to find the positions of min and max.
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] == min) fromLeftLow = i + 1;
                if (arr[i] == max) fromLeftHigh = i + 1;
            }
            
            
            int allLeft = Math.max(fromLeftLow, fromLeftHigh);
            int allRight = Math.max(arr.length-fromLeftLow, arr.length-fromLeftHigh) + 1;
            int rightOrLeft = Math.min(fromLeftLow, fromLeftHigh) + arr.length-Math.max(fromLeftLow, fromLeftHigh)+1;
            
            
            int result = Math.min(allLeft, Math.min(allRight, rightOrLeft));	// As min() can't take more than 2 arguments
            System.out.println(result);
        }
        scanner.close();
    }
}
