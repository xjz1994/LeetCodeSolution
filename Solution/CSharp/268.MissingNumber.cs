static public int MissingNumber(int[] nums) {
    if (nums.Length == 0) {
        return 0;
    }

    int max = 0;
    int min = Int32.MaxValue;
    int total = 0;
    foreach (int i in nums) {
        total += i;
        min = i < min ? i : min;
        max = i > max ? i : max;
    }
    int rest = max * (max + 1) / 2 - total;
    if (min == 0) {
        return (rest == 0) ? max + 1 : rest;
    } else {
        return min - 1;
    }
}
class Solution {
    public:
        int missingNumber(vector<int> & amp; nums) {
            int x = 0;
            for (int i = 0; i <= nums.size(); i++) x ^= i;
            for (auto n: nums) x ^= n;
            return x;
        }
};