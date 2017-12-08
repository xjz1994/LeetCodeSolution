static public string[] FindWords(string[] words) {
    List<string> resultArr = new List<string>();
    HashSet<char> line1 = new HashSet<char>() { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P' };
    HashSet<char> line2 = new HashSet<char>() { 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L' };
    HashSet<char> line3 = new HashSet<char>() { 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Z', 'X', 'C', 'V', 'B', 'N', 'M' };

    foreach (string str in words) {
        if (Check(str, line3) || Check(str, line2) || Check(str, line1)) {
            resultArr.Add(str);
        }
    }
    return resultArr.ToArray();
}

static public bool Check(string str, HashSet<char> hashSet) {
    foreach (char c in str) {
        if (!hashSet.Contains(c)) {
            return false;
        }
    }
    return true;
}
public class Solution {
    public string[] FindWords(string[] words) {
        var rowOne = new HashSet<char>("qwertyuiop");
        var rowTwo = new HashSet<char>("asdfghjkl");
        var rowThree = new HashSet<char>("zxcvbnm");

        return words.Where(word =>
            word.ToLower().All(rowOne.Contains) ||
            word.ToLower().All(rowTwo.Contains) ||
            word.ToLower().All(rowThree.Contains)).ToArray();
    }
}