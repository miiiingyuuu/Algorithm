function solution(topping) {
    const leftSet = new Set();
    const rightMap = new Map();
    
    for (const top of topping) {
        rightMap.set(top, (rightMap.get(top) || 0) + 1);
    }
    
    let count = 0;
    
    for (let i = 0; i < topping.length - 1; i++) {
        const top = topping[i];
        
        leftSet.add(top);
        
        rightMap.set(top, rightMap.get(top) - 1);
        if (rightMap.get(top) === 0) {
            rightMap.delete(top);
        }
        
        if (leftSet.size === rightMap.size) {
            count++;
        }
    }
    
    return count;
}