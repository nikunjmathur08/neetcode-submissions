#include <unordered_map>
#include <algorithm>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map1;
        for (int i = 0; i < strs.size(); i++) {
            string key = strs[i];
            sort(key.begin(), key.end());
            map1[key].push_back(strs[i]);
        }
        vector<vector<string>> result;

        for (auto& pair: map1) {
            result.push_back(pair.second);
        }

        return result;
    }
};
