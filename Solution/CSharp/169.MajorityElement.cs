public class Solution {
    public int MajorityElement(int[] nums) {
        int length = nums.Length;
        int halfLength = length / 2;
        Dictionary<int, int> d = new Dictionary<int, int>();
        int value = 0;
        int num = 0;
        for (int i = 0; i < length; i++) {
            num = nums[i];
            if (d.TryGetValue(num, out value)) {
                d[num] += 1;
            } else {
                d[num] = 1;
            }
        }

        int element = 0;
        foreach (int i in d.Keys) {
            if (d[i] > halfLength) {
                element = i;
            }
        }
        return element;
    }
}