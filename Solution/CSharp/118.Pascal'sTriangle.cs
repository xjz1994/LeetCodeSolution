static public List<List<int>> Generate(int numRows) {
    List<List<int>> result = new List<List<int>>();
    for (int line = 1; line <= numRows; line++) {
        List<int> list = new List<int>();
        if (line >= 3) {
            list.Add(1);
            int index = 1;
            while (index < line - 1) {
                list.Add(result[line - 2][index - 1] + result[line - 2][index]);
                index++;
            }
            list.Add(1);
        } else if (line == 2) {
            list.Add(1);
            list.Add(1);
        } else if (line == 1) {
            list.Add(1);
        }
        result.Add(list);
    }
    return result;
}