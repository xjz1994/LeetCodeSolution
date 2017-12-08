public static bool IsPowerOfThree(int n) {
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
public static bool IsPowerOfThree(int n) {
    if (n == 1) {
        return true;
    } else if (n == 0 || n % 3 > 0) {
        return false;
    } else {
        return IsPowerOfThree(n / 3);
    }
}
class Solution {
    public:
        bool isPowerOfThree(int n) {
            return (n > 0 && int(log10(n) / log10(3)) - log10(n) / log10(3) == 0);
        }
};