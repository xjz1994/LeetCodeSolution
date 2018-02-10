public class Solution {
    public bool IsPowerOfFour(int num) {
        return (num > 0 && (int) (Math.Log10(num) / Math.Log10(4)) - Math.Log10(num) / Math.Log10(4) == 0);
    }
}