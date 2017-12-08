public static int LongestPalindrome(string s) {
    int length = 0;
    Dictionary<char, int> dictionary = new Dictionary<char, int>();
    int value = 0;
    foreach (char c in s) {
        if (dictionary.TryGetValue(c, out value)) {
            dictionary[c] += 1;
        } else {
            dictionary[c] = 1;
        }
    }

    bool addCenter = false;
    foreach (int val in dictionary.Values) {
        if (addCenter == false && val % 2 != 0) {
            length++;
            addCenter = true;
        }
        if (val > 1) {
            length += (val - val % 2);
        }
    }
    return length;
}