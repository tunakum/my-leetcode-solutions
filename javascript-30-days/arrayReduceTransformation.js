//init++ nums[i+1]

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {

    if (nums.length == 0){
        return init;
        
    }

    for (let i = 0; i < nums.length; i++){
        let result = fn(init, nums[i]);
        init = result;            

    }
    return init;
        
};