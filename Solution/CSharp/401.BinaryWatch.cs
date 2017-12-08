static public List<string> ReadBinaryWatch(int num) {
    List<string> list = new List<string>();
    string s = "";
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 60; j++) {
            if (BitCount(i) + BitCount(j) == num) {
                list.Add(i.ToString() + ":" + NumberToString(j));
            }
        }
    }
    return list;
}

static public int BitCount(int number) {
    int sum = 0;
    while (number > 0) {
        if ((number & amp; 1) == 1) {
            sum++;
        }
        number >>= 1;
    }
    return sum;
}

static public string NumberToString(int number) {
    string s = number.ToString();
    return s.PadLeft(2, '0');
}