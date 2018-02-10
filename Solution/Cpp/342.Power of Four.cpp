class Solution1 {
    public:
        bool isPowerOfFour(int num) {
            return num > 0 && !(num & amp;
                (num - 1)) && (num - 1) % 3 == 0;
        }
};

class Solution2 {
    public:
        bool isPowerOfFour(int num) {
            return num > 0 && !(num & amp;
                (num - 1)) && (num & amp; 0x55555555) == num;
        }
};