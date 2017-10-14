class Solution {
public:
    int numberOfArithmeticSlices(vector<int>&amp; A) {
        int res = 0, len = 2, n = A.size();
        for (int i = 2; i < n; ++i) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                ++len;
            } else {
                if (len > 2) res += (len - 1) * (len - 2) * 0.5;
            }
        }
        if (len > 2) res += (len - 1) * (len - 2) * 0.5;
        return res;
    }
};
    public int NumberOfArithmeticSlices(int[] A)
    {
        int n = A.Length;
        if (n < 3) return 0;
        int[] dp = new int[n];
        int result = 0;
        for (int i = 2; i < n; ++i) {
            if (A[i] - A[i - 1] == A[i - 1] - A[i - 2])
            {
                dp[i] = dp[i - 1] + 1;
            }
            result += dp[i];
        }
        return result;
    }
