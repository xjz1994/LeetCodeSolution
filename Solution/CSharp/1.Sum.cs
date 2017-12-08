public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        if (nums == null || nums.Length < 1) {
            return null;
        }
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (dict.ContainsKey(target - nums[i])) {
                int[] arr = { dict[target - nums[i]], i };
                return arr;
            } else {
                dict[nums[i]] = i;
            }
        }
        return null;
    }
}