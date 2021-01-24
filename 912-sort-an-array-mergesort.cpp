class Solution {
public:
    std::vector<int32_t> sortArray(std::vector<int32_t>& v) {
        mergesort<int32_t>(v, [](int32_t a, int32_t b) -> bool { return a < b; });
        return v;
    }
    
private:
    template <typename T> std::vector<T> merge(std::vector<T> &a, std::vector<T> &b, std::function<bool(T, T)> &cmp) 
    {
        if (a.empty())
        {
            return b;
        }
        else if (b.empty())
        {
            return a;
        }
        else
        {
            std::vector<T> v;
            v.reserve(a.size() + b.size());
            size_t n = 0;
            size_t m = 0;
            
            while (n < a.size() && m < b.size())
            {
                v.push_back(cmp(a[n], b[m]) ? a[n++] : b[m++]);
            }
            
            while (n < a.size())
            {
                v.push_back(a[n++]);
            }
            
            while (m < b.size())
            {
                v.push_back(b[m++]);
            }
            
            return v;
        }
    }
    
    template <typename T> void mergesort(std::vector<T> &v, std::function<bool(T, T)> cmp) 
    {
        if (v.size() <= 1)
        {
            return;
        }
        
        std::vector<T> a(v.begin(), v.begin() + v.size() / 2);
        std::vector<T> b(v.begin() + v.size() / 2, v.end());
        
        mergesort<T>(a, cmp);
        mergesort<T>(b, cmp);
        v = merge<T>(a, b, cmp);
    }
};