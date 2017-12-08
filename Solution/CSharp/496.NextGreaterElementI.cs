public class Solution {
    public int[] NextGreaterElement(int[] findNums, int[] nums) {
        int[] resultArr = new int[findNums.Length];
        Dictionary<int, int> indexDict = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            indexDict[nums[i]] = i;
        } {
            int num = -1;
            for (; index < nums.Length; index++) {
                if (nums[index] > findNums[i]) {
                    num = nums[index];
                    break;
                }
            }
            resultArr[i] = num;
        }
        return resultArr;
    }
}