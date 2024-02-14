package codeforcesJavaProject;

import java.util.Scanner;

public class _1551B1_Wonderful_Coloring_1  {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int testCases = scanner.nextInt();

        while (testCases-- > 0) {
            StringBuilder colorSet1 = new StringBuilder();
            StringBuilder colorSet2 = new StringBuilder();
            String inputString = scanner.next();

            for (int i = 0; i < inputString.length(); i++) {
                String currentChar = Character.toString(inputString.charAt(i));

                if (!colorSet1.toString().contains(currentChar)) {
                    colorSet1.append(currentChar);
                } else if (!colorSet2.toString().contains(currentChar)) {
                    colorSet2.append(currentChar);
                }
            }
            int no_of_letters_colored_red_or_green = (colorSet1.length() + colorSet2.length()) / 2;
            System.out.println(no_of_letters_colored_red_or_green);
        }
        scanner.close();
    }
}
