public class Solution {
    public int RemoveDuplicates(int[] nums) {
        List<int> list = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (i >= 1 && nums[i] != nums[i - 1]) {
                list.Add(nums[i]);
            } else if (i == 0) {
                list.Add(nums[i]);
            }
        }
        for (int i = 0; i < list.Count; i++) { }
        return list.Count;
    }
}