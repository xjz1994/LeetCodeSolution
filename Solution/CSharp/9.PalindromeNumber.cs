public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) return false;
        if (x == 0) return true;

        int num = x;
        int div = 1;
        while (num >= 10) {
            num /= 10;
            div *= 10;
        }

        while (x > 0) {
            int left = x / div;
            int right = x % 10;

            if (left != right) {
                return false;
            }

            x = (x % div) / 10;
            div = div / 100;

            Console.WriteLine(x);
            Console.WriteLine(div);
        }
        return true;
    }
}
public boolean isPalindrome1(int x) {
    if (x < 0 || (x != 0 && x % 10 == 0)) return false;
    int rev = 0;
    while (x > rev) {
        rev = rev * 10 + x % 10;
        x = x / 10;
    }
    return (x == rev || x == rev / 10);
}