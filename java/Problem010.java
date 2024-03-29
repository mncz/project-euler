// Summation of Primes

public class Problem010 {
    public static boolean isPrime(int n) {
        if (n <= 1)
            return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }

        return true;
    }

    public static void main(String[] args) {
        long sum = 0;

        for (int i = 2; i < 2000000; i++) {
            if (isPrime(i))
                sum += i;
        }

        System.out.println(sum);
    }
}
