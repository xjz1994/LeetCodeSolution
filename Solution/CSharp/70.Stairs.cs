    public int ClimbStairs(int n) {
        if (n == 0)
            return 0;
        int pre = 0;
        int cur = 1;
        int tempCur = 0;
        for (int i = 1; i <= n; i++) {
            tempCur = cur;
            cur = pre + cur;
            pre = tempCur;
            return cur;
        }
        static public int[] Fibonacci(int n) {
            int[] arr = new int[n + 1];
            arr[0] = 0;
            arr[1] = 1;
            for (int i = 2; i < n + 1; i++) {
                arr[i] = arr[i - 1] + arr[i - 2];
            }
            return arr;
        }
    }