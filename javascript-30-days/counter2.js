//anlık olan sayı üzerinden ilerlemek gerekebilir.


/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let currentCount = init;
    return{
        increment : function() {
            currentCount +=1;
            return currentCount;
        },
        decrement : function() {
            currentCount -= 1;
            return currentCount;
        },
        reset : function() {
            currentCount = init;
            return currentCount;
        }
        
        };
    };


/*const counter = createCounter(5);
console.log(counter.increment()); // 6
console.log(counter.increment()); // 7
console.log(counter.decrement()); // 6
console.log(counter.reset());*/