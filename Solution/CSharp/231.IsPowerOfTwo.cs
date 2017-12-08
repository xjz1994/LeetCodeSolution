public class Solution {
    public boolean IsPowerOfTwo(int n) {
        return n > 0 && ((n & amp;
            (n - 1)) == 0);
    }
}