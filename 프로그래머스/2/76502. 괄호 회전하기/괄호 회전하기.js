function solution(s) {
    let count = 0;
    const len = s.length;
    
    function rotateLeft(str, x) {
        return str.slice(x) + str.slice(0, x);
    }
    
    function isCorrectBrackets(str) {
        const stack = [];
        const pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        };
        
        for (let i = 0; i < str.length; i++) {
            const char = str[i];
            
            if (char === '(' || char === '{' || char === '[') {
                stack.push(char);
            }
            
            else if (char === ')' || char === '}' || char === ']') {
                if (stack.length === 0 || stack.pop() !== pairs[char]) {
                    return false;
                }
            }
        }
        
        return stack.length === 0;
    }
    
    for (let x = 0; x < len; x++) {
        const rotated = rotateLeft(s, x);
        if (isCorrectBrackets(rotated)) {
            count++;
        }
    }
    
    return count;
}