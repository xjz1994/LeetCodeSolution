public class Solution {
    public string AddStrings(string num1, string num2) {
        string s = "";
        int maxLength = Math.Max(num1.Length, num2.Length);
        num1 = num1.PadLeft(maxLength, '0');
        num2 = num2.PadLeft(maxLength, '0');

        int carry = 0;
        int digit = 0;
        int i = maxLength - 1;
        while (i >= 0 || carry > 0) {
            digit = carry;
            if (i >= 0) {
                digit += ((int) num1[i] - 48) + ((int) num2[i] - 48);
            }
            if (digit >= 10) {
                carry = digit / 10;
            } else {
                carry = 0;
            }
            s = (digit % 10).ToString() + s;
            i--;
        }
        return s;
    }
}