static public int ArrangingCoins(int n) {
    return (int) ((Math.Sqrt(8 * (long) n + 1) - 1) / 2);
}