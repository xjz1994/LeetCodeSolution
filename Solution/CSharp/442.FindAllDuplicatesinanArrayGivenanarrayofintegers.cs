public class Solution {
    public IList<int> FindDuplicates(int[] nums) {
        List<int> list = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            nums[Math.Abs(nums[i]) - 1] *= -1;
            if (nums[Math.Abs(nums[i]) - 1] > 0) {
                list.Add(Math.Abs(nums[i]));
            }
        }
        return list;
    }
}