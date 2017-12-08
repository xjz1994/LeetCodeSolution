public class Solution {
    public string ReverseStr(string s, int k) {
        char[] cArr = s.ToArray();
        for (int left = 0; left < cArr.Length; left += 2 * k) {
            for (int i = left, j = Math.Min(left + k - 1, cArr.Length - 1); i < j; i++, j--) {
                char tmp = cArr[i];
                cArr[i] = cArr[j];
                cArr[j] = tmp;
            }
        }
        return new string(cArr);
    }
}