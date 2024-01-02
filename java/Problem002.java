// Even Fibonacci Numbers

public class Problem002 {
    public static void main(String[] args) {
        int a = 1, b = 1, sum = 0;

        while (b < 4000000) {
            int c = a + b;

            if (c % 2 == 0)
                sum += c;
            
            a = b;
            b = c;
        }

        System.out.println(sum);
    }
}
