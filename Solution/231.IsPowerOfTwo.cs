public class Solution {  
    public boolean IsPowerOfTwo(int n) {  
       return n > 0 &amp;&amp; ((n &amp; (n - 1)) == 0 );  
    }  
}  
