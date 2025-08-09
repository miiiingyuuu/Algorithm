function solution(arr) {
    const minVal = Math.min(...arr);
    
    arr.splice(arr.indexOf(minVal), 1);
    
    if (arr.length < 1) {
        return [-1];
    }
    
    return arr; 
}