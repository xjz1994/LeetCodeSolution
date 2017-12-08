public class Solution {
    public int MaxProfit(int[] prices) {
        int sum = 0;
        for (int tail = prices.Length - 1; tail >= 0;) {
            int head = tail - 1;
            while (head > 0 && prices[head] < prices[head + 1] && prices[head] > prices[head - 1]) {
                head--;
            }
            if (head >= 0) {
                int diff = prices[tail] - prices[head];
                if (diff > 0) {
                    sum += diff;
                }
            }
            tail = head;
        }
        return sum;
    }
}