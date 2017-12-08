public int FindContentChildren(int[] g, int[] s) {
    Array.Sort(g);
    Array.Sort(s);
    int feed = 0;
    int childNum = g.Length;
    int cookiesNum = s.Length;
    for (int i = 0; i < cookiesNum; i++) {
        if (feed >= childNum) {
            break;
        }
        if (s[i] >= g[feed]) {
            feed++;
        }
    }
    return feed;
}