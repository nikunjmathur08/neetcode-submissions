#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map1;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            auto it = map1.find(diff);

            if (it != map1.end()) {
                return {map1[diff], i};
            } else { map1[nums[i]] = i; }
        }
    }
};
