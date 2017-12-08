public class Solution {
    public int LengthOfLastWord(string s) {
        int sum = 0;
        bool isWorld = false;
        for (int i = s.Length - 1; i >= 0; i--) {
            if (!isWorld && s[i] != ' ') {
                isWorld = true;
            }
            if (isWorld == true && s[i] != ' ') {
                sum++;
            } else if (isWorld == true && s[i] == ' ') {
                break;
            }
        }
        return sum;
    }
}