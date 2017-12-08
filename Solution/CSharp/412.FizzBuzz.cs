/*
    Write a program that outputs the string representation of numbers from 1 to n.

    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Solution {
    class Solution {
        // bad version
        public IList<string> FizzBuzz(int n) {
            List<string> list = new List<string>();
            for (int index = 1; index <= n; index++) {
                if (index % 3 == 0 && index % 5 == 0) {
                    list.Add("FizzBuzz");
                } else if (index % 3 == 0) {
                    list.Add("Fizz");
                } else if (index % 5 == 0) {
                    list.Add("Buzz");
                } else {
                    list.Add(index.ToString());
                }
            }
            return list;
        }

        // using Linq
        public List<string> FizzBuzz(int n) {
            var list = Enumerable.Range(1, n).Select((i) => {
                if (i % 15 == 0) {
                    return "FizzBuzz";
                } else if (i % 3 == 0) {
                    return "Fizz";
                } else if (i % 5 == 0) {
                    return "Buzz";
                } else {
                    return i.ToString();
                }
            });
            return list.ToList();
        }

        // one line version,using Linq
        public List<string> FizzBuzz(int n) {
            return Enumerable.Range(1, n).Select(i => i % 15 == 0 ? "FizzBuzz" : i % 3 == 0 ? "Fizz" : i % 5 == 0 ? "Buzz" : i.ToString()).ToList();
        }
    }

    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            List<string> res = s.FizzBuzz(15);
            Console.WriteLine(res);
        }
    }
}