public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int index = nums1.Length - 1;
        int index1 = m - 1;
        int index2 = n - 1;
        while (index1 >= 0 && index2 >= 0) {
            if (nums1[index1] > nums2[index2]) {
                nums1[index] = nums1[index1];
                index--;
                index1--;
            } else {
                nums1[index] = nums2[index2];
                index--;
                index2--;
            }
        }

        while (index1 >= 0) {
            nums1[index--] = nums1[index1--];
        } {
            nums1[index--] = nums2[index2--];
        }
    }
}