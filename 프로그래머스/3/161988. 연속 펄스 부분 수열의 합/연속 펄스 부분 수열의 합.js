function solution(sequence) {
    const n = sequence.length;
    let max1 = -Infinity, max2 = -Infinity;
    let cur1 = 0, cur2 = 0;
    
    for (let i = 0; i < n; i++) {
        const pulse1 = i % 2 === 0 ? 1 : -1; // [1, -1, 1, -1...]
        const pulse2 = i % 2 === 0 ? -1 : 1; // [-1, 1, -1, 1...]
        
        cur1 = Math.max(sequence[i] * pulse1, cur1 + sequence[i] * pulse1);
        cur2 = Math.max(sequence[i] * pulse2, cur2 + sequence[i] * pulse2);
        
        max1 = Math.max(max1, cur1);
        max2 = Math.max(max2, cur2);
    }
    
    return Math.max(max1, max2);
}