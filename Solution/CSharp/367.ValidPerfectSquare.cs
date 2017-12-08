public class Solution {
    public bool IsPerfectSquare(int num) {
        long l = 1, r = num / 2 + 1;
        while (l <= r) {
            long m = l + (r - l) / 2;
            long pow = m * m;
            if (pow == num) {
                return true;
            } else if (pow > num) {
                r = m - 1;
            } else if (pow < num) {
                l = m + 1;
            }
            return false;
        }
    }