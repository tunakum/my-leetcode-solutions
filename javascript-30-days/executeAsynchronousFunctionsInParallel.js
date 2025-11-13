/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, reject) => {
        let results = [];
        let count = 0; 

        if(functions.length === 0){
            resolve([]);
            return;
        }

        for(let i = 0; i < functions.length; i++){
            const fn = functions[i];

            fn()
                .then(res => {
                    results[i] = res;
                    count++;  
                    if(count === functions.length){
                        resolve(results);
                    }
                })
                .catch(err => reject(err));
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */