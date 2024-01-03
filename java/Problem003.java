// Largest Prime Factor

public class Problem003 {
    public static void main(String[] args) {
        long x = 600851475143L, i = 2;

        while (x > 1) {
            if (x % i == 0) {
                x /= i;
            } else {
                i++;
            }
        }

        System.out.println(i);
    }
}
