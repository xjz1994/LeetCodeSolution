using System;
using System.Collections.Generic;

namespace ConsoleApp1 {
    public class Solution {
        public bool AreSentencesSimilar(string[] words1, string[] words2, string[, ] pairs) {
            if (words1.Length != words2.Length)
                return false;

            HashSet<string> set = new HashSet<string>();

            for (int i = 0; i < pairs.GetLength(0); i++)
                set.Add($"{pairs[i, 0]}:{pairs[i, 1]}");

            for (int i = 0; i < words1.Length; i++) {
                if (words1[i] == words2[i])
                    continue;

                if (!set.Contains($"{words1[i]}:{words2[i]}") && !set.Contains($"{words2[i]}:{words1[i]}"))
                    return false;
            }
            return true;
        }
    }

    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            string[] w1 = { "great", "acting", "skills" };
            string[] w2 = { "fine", "talent", "drama" };
            string[, ] p = { { "great", "fine" }, { "drama", "acting" }, { "skills", "talent" }, { "skills", "talent" } };
            Console.WriteLine(s.AreSentencesSimilar(w1, w2, p));
        }
    }
}