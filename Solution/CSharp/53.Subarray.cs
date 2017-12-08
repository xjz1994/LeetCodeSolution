public class Solution {
    public int MaxSubArray(int[] nums) {
        if (nums.Length == 0) {
            return 0;
        }
        for (int i = 0; i < nums.Length; i++) {
            if (sum < 0) {
                sum = nums[i];
            } else {
                sum += nums[i];
            }
            if (sum > max) {
                max = sum;
            }
        }
        return max;
    }