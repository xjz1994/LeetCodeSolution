public class Solution {
    public int FindPoisonedDuration(int[] timeSeries, int duration) {
        int sum = 0;
        for (int i = 1; i < timeSeries.Length; i++) {
            var offset = timeSeries[i] - timeSeries[i - 1];
            sum += offset > duration ? duration : offset;
        }
        return timeSeries.Length > 0 ? sum + duration : sum;
    }
}