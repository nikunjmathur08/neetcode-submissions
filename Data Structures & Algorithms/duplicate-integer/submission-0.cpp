#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> numbers;
        for (int i = 0; i < nums.size(); i++) {
            if (numbers.count(nums[i]) == 0) {
                numbers[nums[i]]++;
            } else { return true; }
        }
        return false;
    }
};