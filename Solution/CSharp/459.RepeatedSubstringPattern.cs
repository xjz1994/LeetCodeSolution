public class Solution {
    public bool RepeatedSubstringPattern(string str) {
        int length = str.Length;
        int[] next = new int[length + 1]; //length+1 =C7=F3=D7=EE=B4=F3=B9=AB=B9=B2=D4=AA=CB=D8=B3=A4=B6=C8=CA=FD=D7=E9
        next[0] = -1;
        int j = 0;
        int k = -1;
        while (j < length) {
            ++j;
            ++k;
            next[j] = k;
        } else {
            k = next[k];
        }
    }
    return next[length] != 0 && next[length] % (length - next[length]) == 0;
}
}