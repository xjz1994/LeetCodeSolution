/**
 Given a list of daily temperatures, produce a list that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]. 
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solution {
    public class Solution {
        public int[] DailyTemperatures(int[] temperatures) {
            int[] res = new int[temperatures.Length];
            Stack<int> stack = new Stack<int>();
            for (int i = 0; i < temperatures.Length; i++) {
                while (!(stack.Count() == 0) && temperatures[i] > temperatures[stack.Peek()]) {
                    int idx = stack.Pop();
                    res[idx] = i - idx;
                }
                stack.Push(i);
            }
            return res;
        }
    }

    public class Solution2 {
        public int[] DailyTemperatures(int[] temperatures) {
            int[] res = new int[temperatures.Length];
            Dictionary<int, int> dict = new Dictionary<int, int>();
            for (var i = temperatures.Length - 1; i >= 0; i--) {
                res[i] = Int32.MaxValue;
                foreach (int key in dict.Keys) {
                    if (temperatures[i] < key) {
                        res[i] = Math.Min(res[i], dict[key] - i);
                    }
                }
                dict[temperatures[i]] = i;
                res[i] = res[i] == Int32.MaxValue ? 0 : res[i];
            }
            return res;
        }
    }

    class Program {
        static void Main(string[] args) {
            Solution s = new Solution();
            int[] arr = { 73, 74, 75, 71, 69, 72, 76, 73 };
            var res = s.DailyTemperatures(arr);
            Console.WriteLine(res);
        }
    }
}