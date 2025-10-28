//Soruya başlamadan önce fonksiyon ve metod syntaxlarına Stack Overflow sitesinden farklı örnekler üzerinden pratik yaptım. 


/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(value){
            if (val === value){
                console.log({"value": true});
                return true;
            }
            else{
                console.log({"error": "Not Equal"});    
                throw new Error("Not Equal")
            }
        },
        notToBe: function(value){
            if (val !== value){
                console.log({"value": true});
                return true;
            }
            throw new Error("Equal")
        }
    };
    
};



// expect(5).toBe(6); // true
// expect(5).notToBe(5); // throws "Equal"
 