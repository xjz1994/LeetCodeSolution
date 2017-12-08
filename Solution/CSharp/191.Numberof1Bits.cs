public int HammingWeight(uint n) {
    int sum = 0;
    while (n > 0) {
        if ((n & amp; 1) == 1) {
            sum++;
        }
        n >>= 1;
    }
    return sum;
}