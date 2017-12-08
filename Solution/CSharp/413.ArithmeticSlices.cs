using System;
using System.Collections.Generic;

namespace ConsoleApp1 {
    public class Solution {
        public int NumberOfArithmeticSlices(int[] A) {
            int n = A.Length;
            if (n < 3) return 0;
            int[] dp = new int[n];
            int result = 0;
            for (int i = 2; i < n; ++i) {
                if (A[i] - A[i - 1] == A[i - 1] - A[i - 2]) {
                    dp[i] = dp[i - 1] + 1;
                }
                result += dp[i];
            }
            return result;
        }
    }

    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            int[] arr = { 1, 2, 3, 4, 5, 6, 7 };
            var res = s.NumberOfArithmeticSlices(arr);
        }
    }
}