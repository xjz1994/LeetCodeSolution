public class Solution {
    public bool IsPowerOfFour(int num) {
        return (num > 0 && (int) (Math.Log10(num) / Math.Log10(4)) - Math.Log10(num) / Math.Log10(4) == 0);
    }
}
class Solution {
    public:
        bool isPowerOfFour(int num) {
            return num > 0 && !(num & amp;
                (num - 1)) && (num - 1) % 3 == 0;
        }
};
class Solution {
    public:
        bool isPowerOfFour(int num) {
            return num > 0 && !(num & amp;
                (num - 1)) && (num & amp; 0x55555555) == num;
        }
};