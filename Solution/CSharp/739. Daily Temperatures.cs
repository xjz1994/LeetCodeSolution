using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solution {
    public class Solution {
        public int[] DailyTemperatures(int[] temperatures) {
            int[] res = new int[temperatures.Length];
            Stack<int> stack = new Stack<int>();
            for(int i = 0; i < temperatures.Length; i++) {
                while(!(stack.Count() == 0) && temperatures[i] > temperatures[stack.Peek()]) {
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
            Dictionary<int,int> dict = new Dictionary<int, int>();
            for(var i = temperatures.Length - 1; i >= 0; i--) {
                res[i] = Int32.MaxValue;
                foreach(int key in dict.Keys) {
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
            int[] arr = {73, 74, 75, 71, 69, 72, 76, 73};
            var res = s.DailyTemperatures(arr);
            Console.WriteLine(res);
        }
    }
}
