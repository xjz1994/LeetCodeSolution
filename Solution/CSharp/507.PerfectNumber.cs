static public bool CheckPerfectNumber(int num) {
    if (num == 0 || num == 1) return false;
    int sum = 1;
    for (int i = 2; i < Math.Sqrt(num); i++) {
        if (num % i == 0) {
            sum += i + num / i;
        }
    }
    return sum == num;
}