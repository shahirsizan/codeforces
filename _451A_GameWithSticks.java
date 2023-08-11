package codeforcesJavaProject;
import java.util.Scanner;

public class _451A_GameWithSticks {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();

        int min = Math.min(n, m);
        if (min % 2 == 0) {
            System.out.println("Malvika");
        } else {
            System.out.println("Akshat");
        }
        scanner.close();
    }
}

