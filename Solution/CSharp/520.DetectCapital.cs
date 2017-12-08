public class Solution {
    public bool DetectCapitalUse(string word) {
        string upCopy = word.ToUpper();
        string lowCopy = word.ToLower();
        if (word == upCopy || word == lowCopy) {
            return true;
        }
        string first = word.Substring(0, 1);
        string last = word.Substring(1, word.Length - 1);
        if (first.ToUpper() == first && last.ToLower() == last) {
            return true;
        }
        return false;
    }
}