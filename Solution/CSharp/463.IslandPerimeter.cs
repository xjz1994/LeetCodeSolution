/**
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:[object Object]
 */

using System;
using System.Collections.Generic;

namespace Solution {
    public class Solution {
        public int IslandPerimeter(int[, ] grid) {
            int res = 0;
            int rowNum = grid.GetLength(0);
            int colNum = grid.GetLength(1);
            if (grid == null || rowNum == 0 || colNum == 0)
                return res;
            for (int row = 0; row < rowNum; row++) {
                for (int col = 0; col < colNum; col++) {
                    if (grid[row, col] == 1) {
                        res += 4;
                        //与别的岛屿相连，总数要-2
                        if (row > 0 && grid[row - 1, col] == 1) res -= 2;
                        if (col > 0 && grid[row, col - 1] == 1) res -= 2;
                    }
                }
            }
            return res;
        }
    }
    class Program {
        static void Main(string[] args) {
            var s = new Solution();
            int[, ] arr = { { 0, 1, 0, 0 },
                { 1, 1, 1, 0 },
                { 0, 1, 0, 0 },
                { 1, 1, 0, 0 }
            };
            var res = s.IslandPerimeter(arr);
        }
    }
}