public class Solution {
    public bool IsIsomorphic(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }
        Dictionary<char, int> set = new Dictionary<char, int>();
        List<int> parS = new List<int>();
        int num = 1;
        foreach (var i in s) {
            int val;
            set.TryGetValue(i, out val);
            if (val != 0) {
                parS.Add(set[i]);
            } else {
                set[i] = num;
                parS.Add(set[i]);
                num++;
            }
        }

        List<int> parT = new List<int>();
        set.Clear();
        num = 1;
        foreach (var i in t) {
            int val;
            set.TryGetValue(i, out val);
            if (val != 0) {
                parT.Add(set[i]);
            } else {
                set[i] = num;
                parT.Add(set[i]);
                num++;
            }
        }

        for (var i = 0; i < parS.Count; i++) {
            if (parT[i] != parS[i]) {
                return false;
            }
        }
        return true;
    }
}