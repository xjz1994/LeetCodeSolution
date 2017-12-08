public class Solution {
    public int DistributeCandies(int[] candies) {
        if (candies.Length == 0) {
            return 0;
        }
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < candies.Length; i++) {
            int value = 0;
            int key = candies[i];
            dict.TryGetValue(key, out value);
            if (value > 0) {
                dict[key]++;
            } else {
                dict[key] = 1;
            }
        }
        return dict.Count >= candies.Length / 2 ? candies.Length / 2 : dict.Count;
    }
}