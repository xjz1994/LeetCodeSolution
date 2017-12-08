public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            int index;
            if (dict.TryGetValue(nums[i], out index)) {
                if (i - index <= k) {
                    return true;
                }
            }
            dict[nums[i]] = i;
        }
        return false;
    }
}