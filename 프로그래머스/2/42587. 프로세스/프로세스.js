function solution(priorities, location) {
    let q = priorities.map((priority, index) => ({ priority, index }));
    let ans = 0;
    
    while (q.length > 0) {
        const current = q.shift();
        const higher = q.some(item => item.priority > current.priority);
        
        if (higher) {
            q.push(current);
        } else {
            ans++;
            if (current.index === location) {
                return ans
            }
        }
    }
}