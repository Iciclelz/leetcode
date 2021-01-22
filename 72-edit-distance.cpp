class Solution {
public:
    int32_t minDistance(std::string word1, std::string word2) {
        size_t m = word1.size() + 1;
        size_t n = word2.size() + 1;
        
        std::map<std::pair<size_t, size_t>, size_t> d;
        for (size_t i = 0; i < m; ++i)
        {
            d[std::make_pair(i, 0)] = i;
        }
        
        for (size_t j = 0; j < n; ++j)
        {
            d[std::make_pair(0, j)] = j;
        }
        
        for (size_t j = 1; j < n; ++j)
        {
            for (size_t i = 1; i < m; ++i)
            {
                auto minimum = [](size_t x, size_t y, size_t z) {return std::min(std::min(x, y), z);};
                auto cost = word1.at(i - 1) == word2.at(j - 1) ? 0 : 1;
                d[std::make_pair(i, j)] = minimum(d[std::make_pair(i-1, j)] + 1, d[std::make_pair(i, j-1)] + 1, d[std::make_pair(i-1, j-1)] + cost);
            }
        }
        
        return d[std::make_pair(m-1, n-1)];
    }
};