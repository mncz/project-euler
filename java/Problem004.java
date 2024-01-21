// Largest Palindrome Product

public class Problem004 {
    public static boolean isPalindrome(int n) {
        String s = String.valueOf(n);
        int i = 0, j = s.length() - 1;

        while (i < j) {
            if (s.charAt(i) != s.charAt(j))
                return false;
            
                i++;
                j--;
        }

        return true;
    }

    public static void main(String[] args) {
        int ans = 0;

        for (int i = 100; i < 1000; i++) {
            for (int j = 100; j < 1000; j++) {
                int p = i * j;

                if (isPalindrome(p))
                    ans = ans > p ? ans : p;
            }
        }

        System.out.println(ans);
    }
}
