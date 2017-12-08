/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {
    public int FirstBadVersion(int n) {
        var res = -1;
        var low = 1;
        var high = n;
        while (low <= high) {
            var mid = low + (high - low) / 2;
            if (IsBadVersion(mid)) {
                res = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return res;
    }
}