public class Solution {
    public IList<int> FindDisappearedNumbers(int[] nums) {
        List<int> list = new List<int>();
        int length = nums.Length;
        int[] arr = new int[length];
        for (int i = 0; i < length; i++) {
            arr[nums[i] - 1] += 1;
        }
        for (int i = 0; i < length; i++) {
            if (arr[i] == 0) {
                list.Add(i + 1);
            }
        }
        return list;
    }
}