// js üzerinde array işlemlerini araştırdım
//mapping function matematiksel olarak nedir diye internet üzerinden araştırdım

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const returnArray = [];
    
    for(let i = 0; i < arr.length; i++){
        let result = fn(arr[i], i);
        returnArray[i] = result;
    
    }    

    return returnArray;
    
};