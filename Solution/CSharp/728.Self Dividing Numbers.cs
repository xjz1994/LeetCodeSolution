using System;
using System.Collections.Generic;

namespace ConsoleApp1 {
    class Program {

        public static List<int> SelfDividingNumbers(int left, int right) {
            List<int> res = new List<int>();
            for (int i = left; i <= right; i++) {
                if (IsDividingNumbers(i)) {
                    res.Add(i);
                }
            }
            return res;
        }

        public static bool IsDividingNumbers(int number) {
            var d = 1;
            while (d < number) {
                var num = (number / d) % 10;
                if (num == 0 || number % num != 0) {
                    return false;
                }
                d *= 10;
            }
            return true;
        }

        static void Main(string[] args) {
            var res = SelfDividingNumbers(1, 21);
            Console.Write(res);
        }
    }
}