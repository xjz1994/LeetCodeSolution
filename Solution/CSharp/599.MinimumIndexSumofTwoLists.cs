public class Solution {
    public string[] FindRestaurant(string[] list1, string[] list2) {

        List<Pair> listPair1 = new List<Pair>();

        for (int i = 0; i < list1.Length; i++) {
            Pair pair = new Pair(list1[i], i);
            listPair1.Add(pair);
        }

        List<string> lowestMatchList = new List<string>();
        int lowestMatchIndex = Int32.MaxValue;
        for (int i = 0; i < list2.Length; i++) {
            foreach (Pair pair in listPair1) {
                string restaurant = list2[i];
                if (restaurant == pair.Restaurant) {
                    int sum = i + pair.Index;

                    if (sum == lowestMatchIndex) {

                        lowestMatchList.Add(restaurant);
                    } else if (sum < lowestMatchIndex) {
                        lowestMatchIndex = sum;
                        if (lowestMatchList.Count > 0) {
                            lowestMatchList.Remove(lowestMatchList[0]);
                        }
                        lowestMatchList.Add(restaurant);
                    }
                }
            }
        }
        return lowestMatchList.ToArray();

    }

    public class Pair {
        public string Restaurant { get; set; }
        public int Index { get; set; }
        public Pair(string restaurant, int index) {
            Restaurant = restaurant;
            Index = index;
        }
    }
}