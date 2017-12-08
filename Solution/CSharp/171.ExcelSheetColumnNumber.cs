static public int TitleToNumber(string s) {
    int number = 0;
    int deliver = 1;
    char[] chars = s.ToCharArray();
    int length = chars.Length;
    for (int i = length - 1; i >= 0; i--) {
        number += (chars[i] - 65 + 1) * deliver;
        deliver *= 26;
    }
    return number;
}