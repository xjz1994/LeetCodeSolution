public class Solution {
    public bool IsPowerOfThree(int n) {
        if (n == 1) {
            return true;
        }
        double num = n;
        bool isPower = false;
        while (num >= 1) {
            num = num / 3;
            if (num == 1 && num == (int) num) {
                return true;
            }
        }
        return isPower;
    }
}

public class Solution2 {
    public bool IsPowerOfThree(int n) {
        if (n == 1) {
            return true;
        } else if (n == 0 || n % 3 > 0) {
            return false;
        } else {
            return IsPowerOfThree(n / 3);
        }
    }
}