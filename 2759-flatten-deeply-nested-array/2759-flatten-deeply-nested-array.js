/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const result = []
    if(n==0) return arr
  for(let value of arr){
    if(Array.isArray(value)){
    
      result.push(...flat(value,n-1))
    }
    else {
      result.push(value)
    }
  }
  return result;
};