class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        
        std::vector<char> v(t.begin(), t.end());
        
        for (size_t n = 0; n < s.size(); ++n)
        {
            for (int i = 0 ; i < v.size(); ++i)
            {
                if (s.at(n) == v.at(i))
                {
                    v.erase(v.begin() + i);
                    break;
                }
            }
        }
        
        return v.size() == 0;
    }
};