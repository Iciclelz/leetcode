class Solution {
public:
    string reverseWords(string s) {
        s.erase(0, s.find_first_not_of(' ')); //ltrim()
        s.erase(s.find_last_not_of(' ') + 1); //rtrim()
        
        for (size_t n = 0; n < s.size(); ++n)
        {
            if (s.at(n) == ' ' && (n + 1 < s.size()) && s.at(n + 1) == ' ')
            {
                s.erase(s.begin() + n--);
            }
        }
        
        for (size_t n = 0; n < (s.size() / 2); ++n)
        {
            std::swap(s.at(n), s.at(s.size() - n - 1));
        }
        
        size_t p = 0;
        for (size_t n = 0; n < s.size() + 1; ++n) 
        {
            if (s.size() == n || s.at(n) == ' ')
            {
                for (size_t m = 0; m < ((n - p) / 2); ++m)
                {
                    std::swap(s.at(p + m), s.at(n - m - 1));
                }
                p = n + 1;
            }
        }
        
        return s;
    }
};