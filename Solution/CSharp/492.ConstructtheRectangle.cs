public class Solution {
    public int[] ConstructRectangle(int area) {
        if (area == 0) {
            int[] arr = { };
            return arr;
        }
        int[] result = { area, 1 };
        for (int height = 1; height <= area; height++) {
            if (area % height == 0) {
                int width = area / height;
                if (width < height) {
                    break;
                } else if (width - height < result[0] - result[1]) {
                    result[0] = width;
                    result[1] = height;
                }
            }
        }

        return result;
    }