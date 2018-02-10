public class Solution {
    public void MoveZeroes(int[] nums) {
        int length = nums.Length;
        for (int i = 0; i < length; i++) {
            for (int j = i; j < length; j++) {
                if (nums[i] == 0) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }
}