static public bool IsAnagram(string s, string t) {
    int sLength = s.Length;
    int tLength = t.Length;
    if (sLength != tLength) {
        return false;
    }

    char c = ' ';
    int value = 0;
    Dictionary<char, int> d = new Dictionary<char, int>();
    for (int i = 0; i < sLength; i++) {
        c = s[i];
        if (d.TryGetValue(c, out value)) {
            d[c] += 1;
        } else {
            d[c] = 1;
        }
        c = t[i];
        if (d.TryGetValue(c, out value)) {
            d[c] += 1;
        } else {
            d[c] = 1;
        }
    }

    foreach (int i in d.Values) {
        if (i % 2 != 0) {
            return false;
        }
    }
    return true;
}
public class Solution {
    public bool IsAnagram(string s, string t) {
        int sLength = s.Length;
        int tLength = t.Length;
        if (sLength != tLength) {
            return false;
        }

        char[] sChars = s.ToCharArray();
        char[] tChars = t.ToCharArray();

        Array.Sort(sChars);
        Array.Sort(tChars);

        for (int i = 0; i < sLength; i++) {
            if (sChars[i] != tChars[i]) {
                return false;
            }
        }
        return true;
    }
}