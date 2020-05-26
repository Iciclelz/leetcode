/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    
    let set = new Set();
    
    for (let n = 0; n < nums.length; ++n)
    {
        set.add(nums[n]);
    }
    
    return set.size != nums.length;
};