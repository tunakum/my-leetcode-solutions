// Reviewed javascript.info/promise-basics to strengthen understanding of promises before solving this
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    
    let promise = new Promise(function(resolve, reject){
        setTimeout(() => resolve(), millis);
    });
    return promise;
};

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */