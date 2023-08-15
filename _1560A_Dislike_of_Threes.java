package codeforcesJavaProject;

import java.util.Scanner;

public class _1560A_Dislike_of_Threes{
    public static void main(String[] args) {
    	
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int i = 0; i < t; i++) {
            int k = scanner.nextInt();
            int result = kthGoodNumber(k);
            System.out.println(result);
        }
        
        scanner.close();
    }
    
    public static int kthGoodNumber(int k) {
    	int c = 0;
    	int num = 0;
    	while(c < k) {
    		num++;
    		if ( (num%10 != 3) && (num%3 != 0) ) {   //	Numbers that he likes
    			c++;
    		} 
    	}
        return num;
    }
      
}
