static public int NumberOfBoomerangs(int[, ] points) {
    int number = 0;
    int disSqrt = 0;
    int count = points.GetLength(0);
    for (int i = 0; i < count; i++) {
        Dictionary<int, int> dic = new Dictionary<int, int>();
        for (int j = 0; j < count; j++) {
            if (i == j) {
                continue;
            }

            disSqrt = (points[i, 0] - points[j, 0]) * (points[i, 0] - points[j, 0]) -
                (points[i, 1] - points[j, 1]) * (points[i, 1] - points[j, 1]);

            if (dic.ContainsKey(disSqrt)) {
                dic[disSqrt]++;
            } else { }
        }

        foreach (int value in dic.Values) {
            number += value * (value + 1);
        }
    }
    return number;
}