public class Solution {
    public int MaximumProduct(int[] nums) {
        Array.Sort(nums);
        int length = nums.Length;
        int a = nums[0] * nums[1] * nums[length - 1];
        int b = nums[length - 1] * nums[length - 2] * nums[length - 3];
        return a > b ? a : b;
    }
}