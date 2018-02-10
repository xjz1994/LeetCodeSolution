class Solution {
    public:
        int missingNumber(vector<int> & amp; nums) {
            int x = 0;
            for (int i = 0; i <= nums.size(); i++) x ^= i;
            for (auto n: nums) x ^= n;
            return x;
        }
};