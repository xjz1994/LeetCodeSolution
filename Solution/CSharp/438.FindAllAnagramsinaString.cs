public class Solution {
    public List<int> FindAnagrams(string s, string p) {
        List<int> list = new List<int>();
        if (string.IsNullOrWhiteSpace(s) || s.Length < p.Length)
            return list;
        int sum = 0;
        int[] pArray = new int[26];
        foreach (char c in p) {
            sum = sum + (c - 'a');
            ++pArray[c - 'a'];
        }
        int sum1 = 0;
        int startIndex = 0;

        for (int endIndex = 0; endIndex < s.Length; endIndex++) {
            if (pArray[s[endIndex] - 'a'] == 0) {
                sum1 = 0;
                startIndex = endIndex + 1;
                continue;
            }
            if (endIndex - startIndex + 1 == p.Length) {
                if (sum1 == sum) list.Add(startIndex);
                sum1 -= s[startIndex++] - 'a';
            }
        }
        return list;
    }
}