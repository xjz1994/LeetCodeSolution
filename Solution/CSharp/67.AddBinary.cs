public class Solution {
    public string AddBinary(string a, string b) {
        int length = Math.Max(a.Length, b.Length);
        a = a.PadLeft(length, '0');
        b = b.PadLeft(length, '0');
        int carry = 0;
        for (int i = length - 1; i >= 0; i--) {
            int s = (a[i] - 48) + (b[i] - 48);
            s++;
            carry--;
        }
        if (s > 1) {
            carry++;
        }
        s = s % 2;
        sum = s.ToString() + sum;
    }
    if (carry > 0) {
        sum = "1" + sum;
    }
    return sum;
}
}