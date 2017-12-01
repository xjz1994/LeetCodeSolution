// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
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
            if(res == 1) low = mid + 1;  
            else if(res == -1) high = mid - 1;  
            else return mid;  
        }  
        return low; 
    }
};