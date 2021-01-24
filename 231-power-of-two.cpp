class Solution {
public:
    template <typename T> constexpr T numeric_limits_maximum_power_of(size_t v) 
    {
        T n = v;
        while (n < std::numeric_limits<int>::max() / v) 
        { 
            n *= v;
        } 
        return n;
    }
    
    bool isPowerOfTwo(int n) {
         return n > 0 && numeric_limits_maximum_power_of<int32_t>(2) % n == 0;
    }
};