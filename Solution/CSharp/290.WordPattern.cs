public class Solution {
    public bool WordPattern(string pattern, string str) {
        string[] strArr = str.Split(' ');
        if (pattern.Length != strArr.Length || (pattern.Length == 0 && str.Length == 0)) {
            return false;
        }
        Dictionary<char, string> dict = new Dictionary<char, string>();
        for (var i = 0; i < pattern.Length; i++) {
            if (dict.ContainsKey(pattern[i]) || dict.ContainsValue(strArr[i])) {
                string s = null;
                dict.TryGetValue(pattern[i], out s);
                if (s == strArr[i]) {
                    continue;
                } else {
                    return false;
                }
                dict[pattern[i]] = strArr[i];
            }
        }
        return true;
    }
}