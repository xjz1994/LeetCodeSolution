static public int IslandPerimeter(int[,] grid) {
	int num = 0;
	int rowNum = grid.GetLength(0) - 1;
	int colNum = grid.GetLength(1) - 1;
	for (int row = 0; row <= rowNum; row++) {
		for (int col = 0; col <= colNum; col++) {
			if (grid[row, col] != 1) continue;
			if (row == 0) {
				num++;
			}
			if (row == rowNum) {
				num++;
			}
			if (col == 0) {
				num++;
			}
				num++;
			}
			if (col - 1 >= 0 &amp;&amp; grid[row, col - 1] == 0) {
				num++;
			}
			if (col + 1 <= colNum &amp;&amp; grid[row, col + 1] == 0) {
				num++;
			}
			if (row - 1 >= 0 &amp;&amp; grid[row - 1, col] == 0) {
				num++;
			}
			if (row + 1 <= rowNum &amp;&amp; grid[row + 1, col] == 0) {
				num++;
			}
		}
	}
	return num;
}
