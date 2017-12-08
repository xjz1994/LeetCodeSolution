public int MinMoves(int[] nums) {
    int move = 0;
    int length = nums.Length;
    int min = nums[0];
    for (int i = 0; i < length; i++) {
        min = Math.Min(min, nums[i]);
    }
    for (int i = 0; i < length; i++) {
        move += nums[i] - min;
    }
    return move;
}