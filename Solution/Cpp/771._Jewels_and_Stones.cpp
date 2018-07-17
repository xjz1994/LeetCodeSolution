#include <stdio.h>
#include <iostream>
#include <set>

using namespace std;

class Solution
{
  public:
    int numJewelsInStones(string J, string S)
    {
        int res = 0;
        set<char> s = set<char>();
        for (int i = 0; i < J.size(); i++)
        {
            s.insert(J[i]);
        }
        for (int i = 0; i < S.size(); i++)
        {
            if (s.find(S[i]) != s.end())
            {
                res++;
            }
        }
        return res;
    }
};

int main()
{
    Solution solution = Solution();
    string j = "hello";
    string s = "world";
    int res = solution.numJewelsInStones(j, s);
    std::cout << res << std::endl;
}