class Solution {
public:
    std::vector<int32_t> sortArray(std::vector<int32_t>& v) {
        heapsort<int32_t>(v, [](int32_t a, int32_t b) -> bool { return a < b; });
        return v;
    }
    
private:
    template <typename T> void heapify(std::vector<T> &v, size_t heap_size, int64_t i, std::function<bool(T, T)> &cmp) 
    {
        size_t n = i;
        size_t left = 2 * i + 1;
        size_t right = 2 * i + 2;

        if (left < heap_size && !cmp(v.at(left), v.at(n)))
        {
            n = left;
        }
        
        if (right < heap_size && !cmp(v.at(right), v.at(n)))
        {
            n = right;
        }
        
        if (n != i) 
        {
            std::swap(v.at(i), v.at(n));
            heapify(v, heap_size, n, cmp);
        }
    }
    
    
    template <typename T> void heapsort(std::vector<T> &v, std::function<bool(T, T)> cmp) 
    {
        for (int64_t n = v.size() / 2 - 1; n >= 0; --n)
        {
            heapify(v, v.size(), n, cmp);
        }
        
        for (int64_t n = v.size() - 1; n >= 0; --n) 
        {
            std::swap(v.at(0), v.at(n));
            heapify(v, n, 0, cmp);
        }
    }
};