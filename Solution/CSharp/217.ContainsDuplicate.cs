public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        int length = nums.Length;
        int num = 0;
        Dictionary<int, int> d = new Dictionary<int, int>();
        for (int i = 0; i < length; i++) {
            num = nums[i];
            if (d.TryGetValue(num, out value)) {
                return true;
            } else {
                d[num] = 1;
            }
            return false;
        }
    }