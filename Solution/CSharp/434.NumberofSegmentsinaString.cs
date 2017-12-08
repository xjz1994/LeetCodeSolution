public class Solution {
    public int CountSegments(string s) {
        int sum = 0;
        int newIndex = 0;
        for (int i = 0; i < s.Length; i++) {
            if (s[i] != ' ') {
                newIndex = i;
                while (newIndex < s.Length && s[newIndex] != ' ') {
                    newIndex++;
                }
                sum++;
                i = newIndex;
            }
        }
        return sum;
    }
}