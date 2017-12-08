public class Solution {
    public int HammingDistance(int x, int y) {
        int distance = 0;
        string sX = Convert.ToString(x, 2);
        string sY = Convert.ToString(y, 2);

        sX = sX.PadLeft(maxLength, '0');
        sY = sY.PadLeft(maxLength, '0');

        for (int i = 0; i < maxLength; i++) {
            if (sX[i] != sY[i]) {
                distance++;
            }
        }

        return distance;
    }
}