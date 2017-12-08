/*
    Given an array of integers, every element appears twice except for one. Find that single one.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solution {
    class Solution {

        // using Array.Sort O(nlogn)
        public int SingleNumber(int[] nums) {
            int num = 0;
            int length = nums.Length;
            if (length == 1) {
                return nums[0];
            }
            Array.Sort(nums);
            for (int i = 0; i < length; i += 2) {
                if (i + 1 < length) {
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
            }
        }

        // using Dictionary O(n)
        public int SingleNumber(int[] nums) {
            Dictionary<int, int> dict = new Dictionary<int, int>();
            foreach (var i in nums) {
                if (dict.ContainsKey(i)) {
                    dict[i]++;
                } else {
                    dict[i] = 1;
                }
            }

            int res = -1;
            foreach (var i in dict.Keys) {
                if (dict[i] == 1) {
                    res = i;
                    break;
                }
            }
            return res;
        }
    }

    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            int[] arr = { 1, 2, 3, 4, 4 };
            var res = s.SingleNumber(arr);
            Console.WriteLine(res);
        }
    }
}