public class Solution {
    public string ConvertToBase7(int num) {
        if (num == 0) {
            return "0";
        }
        int number = Math.Abs(num);
        string str = "";
        while (number > 0) {
            int n = number % 7;
            str = n.ToString() + str;
            number /= 7;
        }
        if (num < 0) {
            str = "-" + str;
        }
        return str;
    }
}