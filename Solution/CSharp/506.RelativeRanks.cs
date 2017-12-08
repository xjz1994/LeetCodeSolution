static public string[] FindRelativeRanks(int[] nums) {
        int[] ranks = new int[nums.Length];
        Array.Copy(nums, ranks, nums.Length);
        Array.Sort(ranks, (int a, int b) => { return b - a; });

        Dictionary<int, int> dict = new Dictionary<int, int>();
        for (int i = 0; i < ranks.Length; i++) {
            dict[ranks[i]] = i + 1;
        }

        string[] resultArr = new string[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            int rank = dict[nums[i]];
            if (rank > 3) {
                resultArr[i] = rank.ToString();
            } else {
                switch (rank) {
                    case 1:
                        resultArr[i] = "Gold Medal";
                        break;
                    case 2:
                        resultArr[i] = "Silver Medal";
                        break;
                    case 3:
                        resultArr[i] = "Bronze Medal";
                        break;
                }
            }
            return resultArr;
        }