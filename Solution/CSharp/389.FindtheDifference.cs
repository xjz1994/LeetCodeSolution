public char FindTheDifference(string s, string t) {
    char differenceChar = ' ';
    Dictionary<char, int> d = new Dictionary<char, int>();
    char[] sArr = s.ToCharArray();
    char[] tArr = t.ToCharArray();
    int sLength = sArr.Length;
    int tLength = tArr.Length;
    for (int i = 0; i < sLength; i++) {
        char c = sArr[i];
        int v = 0;
        if (d.TryGetValue(c, out v)) {
            d[c] = v + 1;
        } else {
            d.Add(c, 1);
        }
    }
    for (int i = 0; i < tLength; i++) {
        char c = tArr[i];
        int v = 0;
        if (d.TryGetValue(c, out v)) {
            d[c] = v + 1;
        } else {
            d.Add(c, 1);
        }
    }
    foreach (char c in d.Keys) {
        if (d[c] % 2 != 0) {
            differenceChar = c;
            break;
        }
    }
    return differenceChar;
}