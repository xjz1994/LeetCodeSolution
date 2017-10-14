int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int low = 1;  
        int high = n;  
        int res;  
        int mid;  
        while(high > low){  
            mid = low + (high - low) / 2;  
            res = guess(mid);  
            else if(res == -1) high = mid - 1;  
            else return mid;  
        }  
        return low; 
    }
};
