public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        StringBuilder result = new StringBuilder();
        if (strs != null && strs.Length > 0) {
            Array.Sort(strs);
            char[] a = strs[0].ToCharArray();
            char[] b = strs[strs.Length - 1].ToCharArray();
            for (int i = 0; i < a.Length; i++) {
                if (b.Length > i && b[i] == a[i]) {
                    result.Append(b[i]);
                } else {
                    return result.ToString();
                }
            }
            return result.ToString();
        } else {
            return "";
        }
    }
}