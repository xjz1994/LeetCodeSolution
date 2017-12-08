public class Solution {
    public IList<int> GetRow(int rowIndex) {
        List<int> result = new List<int>();
        if (rowIndex >= 0) { result.Add(1); }
        if (rowIndex >= 1) { result.Add(1); }
        for (int index = 2; index <= rowIndex; index++) {
            result.Add(1);
            for (int i = index - 1; i >= 1; i--) {
                result[i] = result[i] + result[i - 1];
            }
        }
        return result;
    }
}