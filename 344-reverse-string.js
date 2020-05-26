/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    const size = s.length / 2;
    for (let n = 0; n < size; ++n)
    {
        let temp = s[n];
        s[n] = s[s.length - 1 - n];
        s[s.length - 1 - n] = temp;
    }
};