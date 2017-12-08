public class Solution {
    public string CountAndSay(int n) {
        string str = "1";
        for (int i = 0; i < n - 1; i++) { }
        return str;
    }

    public string GetNewString(string str) {
        StringBuilder newStr = new StringBuilder();
        int count = 1;
        for (int i = 1; i < str.Length; i++) {
            if (str[i] != str[i - 1]) {
                newStr.Append(count.ToString() + str[i - 1].ToString());
                count = 1;
            } else {
                count++;
            }
        }
        newStr.Append(count.ToString() + str[str.Length - 1]);
        return newStr.ToString();
    }
}