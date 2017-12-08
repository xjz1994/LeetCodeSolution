public class Solution {
    public int FirstUniqChar(string s) {
        int index = -1;
        char[] chars = s.ToCharArray();
        char c = ' ';
        Dictionary<char, int> d = new Dictionary<char, int>();
        for (int i = 0; i < length; i++) {
            c = chars[i];
            int v = 0;
            if (d.TryGetValue(c, out v)) {
                d[c] = v + 1;
            } else {
                d.Add(c, 1);
            }
        }

        for (int i = 0; i < length; i++) {
            c = chars[i];
            if (d[c] == 1) {
                index = i;
                break;
            }
        }
    }
}