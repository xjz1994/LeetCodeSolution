static public int[] CountBits(int n) {
    int[] arr = new int[n + 1];
    arr[0] = 0;

    int pow2 = 2;
    int before = 1;
    for (int i = 1; i < n + 1; i++) {
        if (i == pow2) {
            arr[i] = 1;
            before = 1;
            pow2 <<= 1;
        } else {
            arr[i] = arr[before] + 1;
            before++;
        }
    }

    return arr;
}