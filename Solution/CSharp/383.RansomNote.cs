static public bool CanConstruct(string ransomNote, string magazine) {
    Dictionary<char, int> d = new Dictionary<char, int>();
    char[] mArr = magazine.ToCharArray();
    int mArrLength = mArr.Length;
    for (int i = 0; i < mArrLength; i++) {
        char c = mArr[i];
        int v = 0;
        if (d.TryGetValue(c, out v)) {
            d[c] = v + 1;
        } else {
            d.Add(c, 1);
        }
    }
    char[] rArr = ransomNote.ToCharArray();
    int rArrLength = rArr.Length;
    for (int i = 0; i < rArrLength; i++) {
        char c = rArr[i];
        int v = 0;
        if (!d.TryGetValue(c, out v) || v == 0) {
            return false;
        } else {
            d[c] -= 1;
        }
    }
    return true;
}