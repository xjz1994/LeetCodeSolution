public class Solution {
    public int RomanCharToInt(char c) {
        switch (c) {
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }

    public int RomanToInt(string s) {
        int length = s.Length;
        int i = length - 1;
        int sum = RomanCharToInt(s[i--]);
        while (i >= 0) {
            if (RomanCharToInt(s[i + 1]) > RomanCharToInt(s[i])) {
                sum -= RomanCharToInt(s[i--]);
            } else {
                sum += RomanCharToInt(s[i--]);
            }
        }
        return sum;
    }