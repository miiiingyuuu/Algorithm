function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
    
    const visited = new Set();
    const q = [[begin, 0]];
    
    while (q.length > 0) {
        const [current, count] = q.shift();
        
        if (current === target) {
            return count;
        }
        
        for (const word of words) {
            if (!visited.has(word) && isCovertible(current, word)) {
                visited.add(word);
                q.push([word, count + 1]);
            }
        }
    }
    
    return 0;
}

function isCovertible(word1, word2) {
    let diff = 0;
    
    for (let i = 0; i < word1.length; i++) {
        if (word1[i] != word2[i]) diff++;
        if (diff > 1) return false;
    }
    
    return diff === 1;
}