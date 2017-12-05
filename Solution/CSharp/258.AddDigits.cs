public class Solution {
    public int AddDigits(int num) {
        char[] nums = num.ToString().ToCharArray();
        if(num/10 >= 1){
            int sum = 0;
            foreach(char c in nums){
                sum += (Convert.ToInt32(c) - 48);
            }
            return AddDigits(sum);
        }else{
            return num;
        }
    }
}