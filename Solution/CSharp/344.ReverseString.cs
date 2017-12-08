public class Solution {
    public string ReverseString(string s) {
        char[] cArr = s.ToCharArray();
        int length = cArr.Length;
        int hLength = length / 2;
        for (int i = 0; i < hLength; i++) {
            c = cArr[i];
            cArr[i] = cArr[length - i - 1];
            cArr[length - i - 1] = c;
        }
        return new string(cArr);
    }