function solution(k, score) {
    const hallOfFame = [];
    const result = [];
    
    for (const s of score) {
        hallOfFame.push(s);
        
        hallOfFame.sort((a, b) => a - b);
        
        if (hallOfFame.length > k) {
            hallOfFame.shift();
        }
        
        result.push(hallOfFame[0]);
    }
    
    return result;
}