11103
17987
Easy
joshpowell
public class Solution {
    public string ReverseWords(string s) {
        char[] cArr = s.ToCharArray();
        int left = 0;
        for (int i = 0; i < cArr.Length; i++) {
            if (cArr[i] == ' ' || i == cArr.Length - 1) {
                int right = i == cArr.Length - 1 ? i : i - 1;
                while (left < right) {
                    Swap(left, right, cArr);
                    left++;
                    right--;
                }
                i++;
                left = i;
                right = i;
            }
        }
        return new String(cArr);
    }

    public void Swap(int i, int j, char[] cArr) {
        char c = cArr[i];
        cArr[i] = cArr[j];
        cArr[j] = c;
    }
}