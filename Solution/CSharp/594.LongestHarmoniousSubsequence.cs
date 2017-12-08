5540
14066
Easy
love_Fawn
public class Solution {
    public int FindLHS(int[] nums) {
        if (nums.Length == 0) {
            return 0;
        }
        Array.Sort(nums);
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int num = nums[i];
            int val = 0;
            dict.TryGetValue(num, out val);
            if (val > 0) {
                dict[num]++;
            } else {
                dict[num] = 1;
            }
        }
        int sum = 0;
        int? lastKey = null;
        foreach (int i in dict.Keys) {
            if (lastKey == null) {
                lastKey = i;
                continue;
            }
            int lk = (int) lastKey;
            if (Math.Abs(i - lk) == 1) {
                sum = Math.Max(sum, dict[i] + dict[lk]);
            }
            lastKey = i;
        }
        return sum;
    }
}