/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {

    return async function(...args) {
        let timer = new Promise(function(resolve, reject){
            setTimeout(() => reject("Time Limit Exceeded"), t)
        });

        let result = await Promise.race([
            fn(...args),
            timer
        ]);

        return result;
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */