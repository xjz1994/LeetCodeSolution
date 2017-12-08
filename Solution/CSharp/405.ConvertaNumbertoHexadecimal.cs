static void Main(string[] args) {
    int i = 60;
    string s = "";
    while (i > 0) {
        s = (i % 2).ToString() + s;
        i /= 2;
    }
    Console.WriteLine(Convert.ToString(60, 2)); //c#=D7=AA=BB=BB=B7=BD=B7=A8
    Console.WriteLine(s);
}

public class Solution {
    public string ToHex(int num) {
        if (num == 0) {
            return "0";
        }
        long number = Convert.ToInt64(num);
        if (number < 0) {
            number = UInt32.MaxValue + number + 1; //=C8=A1=B7=B4+1
        }
        char[] hex = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f' };
        string hexString = "";
        long n = 0;
        char c = ' ';
        while (number > 0) {
            n = number % 16;
            c = hex[n];
            hexString = c + hexString;
            number /= 16;
        }
        return hexString;
    }
}