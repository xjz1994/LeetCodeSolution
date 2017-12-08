public int[] Intersection(int[] nums1, int[] nums2) {
    List<int> l = new List<int>();
    List<int> sameList = new List<int>();

    int length = nums1.Length;
    for (int i = 0; i < length; i++) {
        l.Add(nums1[i]);
    }

    length = nums2.Length;
    int num = 0;
    for (int i = 0; i < length; i++) {
        num = nums2[i];
        if (l.Contains(num) && !sameList.Contains(num)) {
            sameList.Add(num);
        }
    }

    int[] list = sameList.ToArray();
    return list;
}