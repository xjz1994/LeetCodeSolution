public void MoveZeroes(int[] nums) {
    int length = nums.Length;
    for (int i = 0; i < length; i++) {
        for (int j = i; j < length; j++) {
            if (nums[i] == 0) { //=C8=E7=B9=FB=B5=C8=D3=DA0=A3=AC=D4=F2=B8=FA=BA=F3=C3=E6=B5=C4=D4=AA=CB=D8=BD=BB=BB=BB
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
}