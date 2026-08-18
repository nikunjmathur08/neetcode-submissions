#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() == t.length()) {
            unordered_map<int, int> map1;
            for (int i = 0; i < s.length(); i++) {
                map1[s[i]]++;
                map1[t[i]]--;
            }
            for (int i = 0; i < s.length(); i++) {
                if(map1[s[i]] == 0) { continue; }
                else { return false; }
            }
            return true;
        } else {
            return false;
        }
    }
};
