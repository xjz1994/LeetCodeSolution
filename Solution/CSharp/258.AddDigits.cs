/*
    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

    For example:

    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

    Follow up:
    Could you do it without any loop/recursion in O(1) runtime? 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solution {

    public class Solution {
        public int AddDigits(int num) {
            char[] nums = num.ToString().ToCharArray();
            if (num / 10 >= 1) {
                int sum = 0;
                foreach (char c in nums) {
                    sum += (Convert.ToInt32(c) - 48);
                }
                return AddDigits(sum);
            } else {
                return num;
            }
        }

        //one line solution
        public int AddDigits(int num) {
            return (num - 1) % 9 + 1;
        }
    }

    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            var res = s.AddDigits(38);
            Console.WriteLine(res);
        }
    }
}