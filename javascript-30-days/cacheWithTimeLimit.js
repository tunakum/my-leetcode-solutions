// Familiar with Map. Researched for of loop syntax.

var TimeLimitedCache = function() {
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    now = Date.now();
    expireTime = now + duration;
    exist = this.cache.has(key);

    this.cache.set(key, {value: value, expireTime: expireTime});

    return exist
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if(!this.cache.has(key)){
        return -1
    }

    data = this.cache.get(key);
    
    if(Date.now() > data.expireTime){
        this.cache.delete(key);
        return -1
    }

    else{
        return data.value
    }

    
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    for(let [key, data] of this.cache){
        if(Date.now() > data.expireTime){
            this.cache.delete(key);
    }
}
    return this.cache.size

};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */