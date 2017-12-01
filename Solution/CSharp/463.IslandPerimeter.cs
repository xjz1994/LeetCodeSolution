using System;
using System.Collections.Generic;

namespace Solution
{
    public class Solution {
        public int IslandPerimeter(int[,] grid) {
            int res = 0;
            int rowNum = grid.GetLength(0);
            int colNum = grid.GetLength(1);
            if(grid == null || rowNum == 0 || colNum == 0)
                return res;
            for (int row = 0; row < rowNum; row++) {
                for (int col = 0; col < colNum; col++) {
                    if(grid[row,col] == 1){
                        res += 4;                        
                        //与别的岛屿相连，总数要-2
                        if(row > 0 && grid[row - 1, col] == 1) res -= 2;
                        if(col > 0 && grid[row, col - 1] == 1) res -= 2;
                    }
                }
            }
            return res;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var s = new Solution();
            int[,] arr = {{0,1,0,0},
                          {1,1,1,0},
                          {0,1,0,0},
                          {1,1,0,0}};
            var res = s.IslandPerimeter(arr);
        }
    }
}

