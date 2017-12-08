using System;
using System.Collections;
using System.Collections.Generic;

namespace Solution {
    public class Solution {
        public class Node {
            public Node(int row, int col) {
                this.row = row;
                this.col = col;
            }
            public int row { get; set; }
            public int col { get; set; }
        }

        public int[, ] FloodFill(int[, ] image, int sr, int sc, int newColor) {
            var baseColor = image[sr, sc];
            if (baseColor == newColor) {
                return image;
            }
            var q = new Queue<Node>();
            q.Enqueue(new Node(sr, sc));
            while (q.Count > 0) {
                var node = q.Dequeue();
                var r = node.row;
                var c = node.col;
                if (r - 1 >= 0 && image[r - 1, c] == baseColor) {
                    q.Enqueue(new Node(r - 1, c));
                }
                if (r + 1 < image.GetLength(0) && image[r + 1, c] == baseColor) {
                    q.Enqueue(new Node(r + 1, c));
                }
                if (c - 1 >= 0 && image[r, c - 1] == baseColor) {
                    q.Enqueue(new Node(r, c - 1));
                }
                if (c + 1 < image.GetLength(1) && image[r, c + 1] == baseColor) {
                    q.Enqueue(new Node(r, c + 1));
                }
                image[r, c] = newColor;
            }
            return image;
        }
    }

    class Program {

        static void Main(string[] args) {
            Solution s = new Solution();

            //int[,] img = {
            //    {1, 1, 1},
            //    {1, 1, 0},
            //    {1, 0, 1}
            //};
            int[, ] img = { { 0, 0, 0 },
                { 0, 1, 1 }
            };
            int sr = 1;
            int sc = 1;
            int newColor = 1;
            int[, ] res = s.FloodFill(img, sr, sc, newColor);
            Console.WriteLine(res);
        }
    }
}