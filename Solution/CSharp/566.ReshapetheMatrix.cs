public class Solution {
    public int[, ] MatrixReshape(int[, ] nums, int r, int c) {
        if (nums.GetLength(0) * nums.GetLength(1) != r * c) {
            return nums;
        }
        Queue<int> list = new Queue<int>();
        for (var i = 0; i < nums.GetLength(0); i++) {
            for (var j = 0; j < nums.GetLength(1); j++) {
                list.Enqueue(nums[i, j]);
            }
        }

        int[, ] newMatrix = new int[r, c];
        for (var i = 0; i < newMatrix.GetLength(0); i++) {
            for (var j = 0; j < newMatrix.GetLength(1); j++) {
                newMatrix[i, j] = list.Dequeue();
            }
        }
        return newMatrix;
    }
}