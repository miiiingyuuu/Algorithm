function solution(number, k) {
    const stack = [];
    let removeCount = 0;
    
    for (let i = 0; i < number.length; i++) {
        const digit = number[i];
        
        while (stack.length > 0 && stack[stack.length - 1] < digit && removeCount < k) {
            stack.pop();
            removeCount++;
        }
        
        stack.push(digit);
    }
    
    return stack.slice(0, number.length - k).join('');
}