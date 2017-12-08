public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        List<int> list = new List<int>();
        List<int> intersectList = new List<int>();
        list = nums1.ToList<int>();

        int num = 0;
        int length = nums2.Length;
        for (int i = 0; i < length; i++) {
            num = nums2[i];
            if (list.Contains(nums2[i])) {
                list.Remove(num);
                intersectList.Add(num);
            }
        }

        int[] intersect = intersectList.ToArray();
        return intersect;
    }
}