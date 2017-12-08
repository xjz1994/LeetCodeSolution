public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int index = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == val) {
                length--;
            } else {
                nums[index++] = nums[i];
            }
        }
        return length;
    }
}