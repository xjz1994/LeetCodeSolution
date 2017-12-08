public class Solution {
    public int GetSum(int a, int b) {
        int sum = 0;
        while (b != 0) {
            sum = a ^ b;
            b = (a & amp; b) << 1;
            a = sum;
        }
        return sum;
    }
}