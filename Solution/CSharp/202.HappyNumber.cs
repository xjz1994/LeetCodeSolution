22
22
22
222
public class Solution {
    public int GetSquareSum(int num) {
        int sum = 0;
        while (num >= 1) {
            if (num >= 10) {
                sum += (num % 10) * (num % 10);
            } else {
                sum += num * num;
            }
            num = num / 10;
        }
        return sum;
    }

    public bool IsHappy(int n) {
        List<int> numberList = new List<int>();
        while (true) {
            n = GetSquareSum(n);
            if (n == 1) {
                return true;
            } else if (numberList.IndexOf(n) >= 0) {
                return false;
            }
            numberList.Add(n);
        }
    }