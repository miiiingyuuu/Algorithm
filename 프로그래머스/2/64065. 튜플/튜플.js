function solution(s) {
    s = s.substring(2, s.length - 2);
    
    const sets = s.split('},{').map(set => set.split(',').map(Number));
    
    sets.sort((a, b) => a.length - b.length);
    
    const result = [];
    const added = new Set();
    
    for (const set of sets) {
        for (const num of set) {
            if (!added.has(num)) {
                added.add(num);
                result.push(num);
            }
        }
    }
    
    return result;
}