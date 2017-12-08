public class Solution {
    public int MaxCount(int m, int n, int[, ] ops) {
        int rowMin = Int32.MaxValue;
        int colMin = Int32.MaxValue;
        if (ops.GetLength(0) == 0) {
            return m * n;
        }
        for (int i = 0; i < ops.GetLength(0); i++) {
            int row = ops[i, 0];
            int col = ops[i, 1];
            if (row > 0) {
                rowMin = Math.Min(rowMin, row);
            } else {
                return 0;
            }
            if (col > 0) {
                colMin = Math.Min(colMin, col);
            } else {
                return 0;
            }
        }
        return rowMin * colMin;
    }
}