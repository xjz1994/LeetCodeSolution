public class Solution {
    public IList<string> FizzBuzz(int n) {
		List<string> list = new List<string>();
		for (int index = 1; index <= n; index++) {//=D2=AA=B4=D31=BF=AA=CA=BC=A3=AC=C1=ED=CD=E2=D2=AA=D7=A2=D2=E20%=C8=CE=D2=E2=CA=FD=D7=D6=B6=BC=CA=C70
			if (index % 3 == 0 &amp;&amp; index % 5 == 0) {
				list.Add("FizzBuzz");
			} else if (index % 3 == 0) {
				list.Add("Fizz");
			} else if (index % 5 == 0) {
				list.Add("Buzz");
			} else {
				list.Add(index.ToString());
			}
		}
		return list;
    }
}
