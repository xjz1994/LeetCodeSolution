static public string ReverseVowels(string s) {
    Stack<char> vowelsStack = new Stack<char>();
    for (int i = 0; i < s.Length; i++) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            vowelsStack.Push(c);
        }
    }

    string rsult = "";
    for (int i = 0; i < s.Length; i++) {
        char c = s[i];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
            rsult += vowelsStack.Pop();
        } else {
            rsult += c;
        }
    }

    return rsult;
}
public class Solution {
    public string ReverseVowels(string s) {
        char[] cArr = s.ToArray();
        int l = 0, r = s.Length - 1;
        while (l < r) {
            while (l < r && !IsVowels(cArr[l])) l++;
            while (l < r && !IsVowels(cArr[r])) r--;

            char temp = cArr[l];
            cArr[l] = cArr[r];
            cArr[r] = temp;
            l++;
            r--;
        }
        return new string(cArr);
    }

    public bool IsVowels(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    }
}