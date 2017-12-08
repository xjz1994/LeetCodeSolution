public class Solution {
    public int[] PlusOne(int[] digits) {
        int plus = 1;
        List<int> resultList = new List<int>();
        for (int i = digits.Length - 1; i >= 0; i--) {
            if (plus > 0) {
                digits[i] += 1;
                if (digits[i] >= 10) {
                    digits[i] = digits[i] % 10;
                } else {
                    plus--;
                }
            }
            resultList.Add(digits[i]);
            if (i == 0 && plus == 1) {
                resultList.Add(1);
            }
        }
        resultList.Reverse();
        return resultList.ToArray();
    }
}