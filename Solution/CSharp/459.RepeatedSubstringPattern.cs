public class Solution {
    public bool RepeatedSubstringPattern(string str) {
        int length = str.Length;
        int[] next = new int[length + 1];
        next[0] = -1;
        int j = 0;
        int k = -1;
        while (j < length) {
            ++j;
            ++k;
            next[j] = k;
        } else {
            k = next[k];
        }
        return next[length] != 0 && next[length] % (length - next[length]) == 0;
    }
}