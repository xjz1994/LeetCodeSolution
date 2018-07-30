#include <stdio.h>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Solution
{
  public:
    int missingNumber(vector<int> nums)
    {
        int x = 0;
        for (int i = 0; i <= nums.size(); i++)
        {
            x ^= i;
        }
        for (auto n : nums)
        {
            x ^= n;
        }
        return x;
    }
};

int main()
{
    return 0;
}