/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let v = 0;
    for (let n = 0; n < nums.length; ++n)
    {
        v ^= nums[n];
    }
    return v;
};