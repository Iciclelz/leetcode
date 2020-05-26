/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    if (nums.size <= 1)
    {
        return false;
    }
    
    let v = new Array();
    
    for (let n = 0; n < nums.length; ++n)
    {
        v.push([nums[n], n]);
    }
 
    
    v.sort((a, b) =>
    {
        return a[0] < b[0]; 
    });

    for (let n = 0; n < v.length - 1 ; ++n)
    {
        if (v[n][0] == v[n+1][0] && 
            Math.abs(v[n][1] - v[n+1][1]) <= k)
        {
            return true;
        }
    }
    
    return false;
};