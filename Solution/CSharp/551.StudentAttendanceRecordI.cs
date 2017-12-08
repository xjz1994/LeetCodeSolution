'A'
'L'
'P'
public class Solution {
    public bool CheckRecord(string s) {
        int lateNum = 0;
        int absentNum = 0;
        foreach (var i in s) {
            if (i == 'L') {
                lateNum++;
            } else {
                lateNum = 0;
                if (i == 'A') {
                    absentNum++;
                }
            }
            if (absentNum > 1 || lateNum > 2) {
                return false;
            }
        }
        return true;
    }
}