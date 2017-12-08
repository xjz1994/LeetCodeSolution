public class Solution {

    public int MaxProfit(int[] prices) {
        if (prices.Length == 0) {
            return 0;
        }
        int low = prices[0];
        int max = 0;
        int length = prices.Length;
        for (int i = 0; i < length; i++) {
            if (prices[i] < low) {
                low = prices[i];
            } else if (prices[i] - low > max) {
                max = prices[i] - low;
            }
        }
        return max;
    }
}