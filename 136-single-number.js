/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    for (let n = 1; n < nums.length; ++n) {
        nums[0] ^= nums[n];
    }
    return nums[0];
};