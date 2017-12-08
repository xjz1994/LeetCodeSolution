static public int FindMaxConsecutiveOnes(int[] nums) {
    if (nums.Length == 0) {
        return 0;
    }
    int maxNumber = 0;
    int number = 0;
    for (int i = 0; i <= nums.Length; i++) {
        if (i != nums.Length && nums[i] == 1) {
            number++;
        } else {
            if (number > maxNumber) {
                maxNumber = number;
            }
            number = 0;
        }
    }
    return maxNumber;
}