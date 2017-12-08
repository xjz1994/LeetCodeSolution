public int FindComplement(int num) {
    int number = 0;
    string s = "";
    while (num > 0) {
        s = ((num % 2) ^ 1).ToString() + s;
        num /= 2;
    }
    for (int i = s.Length - 1; i >= 0; i--)
        number += (Convert.ToInt32(s[i]) - 48) * (int) Math.Pow(2, pow++);
}
return number;
}