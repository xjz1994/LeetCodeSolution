n

public class Solution {
    public int ArrayPairSum(int[] nums) {
        Array.Sort(nums);
        int sum = 0;
        for (int i = 0; i < nums.Length; i += 2) {
            sum += nums[i];
        }
        return sum;
    }
}