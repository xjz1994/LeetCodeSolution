public class Solution {
 &nbsp; &nbsp;public int SingleNumber(int[] nums) {
		int num = 0;
		int length = nums.Length;
		if (length == 1) {
			return nums[0];
		}
		Array.Sort(nums);
		for (int i = 0; i < length; i += 2) {
			if (i+1 < length) {
				if (nums[i] == nums[i + 1]) {
					continue;
				} else {
					num = nums[i];
					break;
				}
			} else {
				num = nums[i];
				break;
			}
		return num;
 &nbsp; &nbsp;}
}
