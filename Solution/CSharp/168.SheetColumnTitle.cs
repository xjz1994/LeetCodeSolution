static public string ConvertToTitle(int n) {
    string s = "";
    char c = ' ';
    while (n > 0) {
        int num = (n - 1) % 26;
        c = Convert.ToChar(num + 65);
        s = c + s;
        n = (n - 1) / 26;
    }
    return s;
}