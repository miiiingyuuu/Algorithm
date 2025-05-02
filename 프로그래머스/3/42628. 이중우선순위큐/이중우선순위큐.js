function solution(operations) {
    const q = [];
    
    for (const op of operations) {
        const [cmd, val] = op.split(' ');
        const num = parseInt(val);
        
        if (cmd === 'I') {
            q.push(num);
        } else if (cmd === 'D') {
            if (q.length === 0) continue;
            
            if (num === 1) {
                const maxIndex = q.indexOf(Math.max(...q));
                q.splice(maxIndex, 1);
            }
            
            else if (num === -1) {
                const minIndex = q.indexOf(Math.min(...q));
                q.splice(minIndex, 1);
            }
        }
    }
    
    if (q.length === 0) return [0, 0];
    
    return [Math.max(...q), Math.min(...q)];
}