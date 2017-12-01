public class Solution {
 &nbsp; &nbsp;public int MaxProfit(int[] prices) {
 &nbsp; &nbsp; &nbsp; &nbsp;if (prices.Length == 0)
 &nbsp; &nbsp; &nbsp; &nbsp;{
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;return 0;
 &nbsp; &nbsp; &nbsp; &nbsp;}
 &nbsp; &nbsp; &nbsp; &nbsp;int low = prices[0];
 &nbsp; &nbsp; &nbsp; &nbsp;int max = 0;
 &nbsp; &nbsp; &nbsp; &nbsp;int length = prices.Length;
 &nbsp; &nbsp; &nbsp; &nbsp;for (int i = 0; i < length; i++)
 &nbsp; &nbsp; &nbsp; &nbsp;{
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;if (prices[i] < low)
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;low = prices[i];
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;else if (prices[i] - low > max)
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;{
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;max = prices[i] - low;
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;}
 &nbsp; &nbsp; &nbsp; &nbsp;}
 &nbsp; &nbsp; &nbsp; &nbsp;return max;
 &nbsp; &nbsp;}
}
