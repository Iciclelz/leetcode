class Solution {
public:
    std::vector<int32_t> sortArray(std::vector<int32_t>& v) {
        quicksort<int32_t>(v, [](int32_t a, int32_t b) -> bool { return a <= b; });
        return v;
    }
    
private:
    template <typename T> size_t partition(std::vector<T> &v, int64_t lo, int64_t hi, std::function<bool(T, T)> &cmp) 
    {
        int64_t i = lo - 1;
       
        for (size_t j = lo; j < hi; ++j)
        {
            if (cmp(v.at(j), v.at(hi)))
            {
                std::swap(v.at(++i), v.at(j));
            }
        }
        
        
        std::swap(v.at(++i), v.at(hi)); 
        return i; 
    }
    
    template <typename T> void quicksort(std::vector<T> &v, int64_t lo, int64_t hi, std::function<bool(T, T)> &cmp) 
    {
        if (lo < hi)
        {
            size_t p = partition<T>(v, lo, hi, cmp);
            
            quicksort<T>(v, lo, p - 1, cmp);
            quicksort<T>(v, p + 1, hi, cmp);
        }
    }
    
    template <typename T> void quicksort(std::vector<T> &v, std::function<bool(T, T)> cmp) 
    {
        quicksort<T>(v, 0, v.size() - 1, cmp);
    }
};