function solution(s) {
    const lastSeen = {};
    
    return s.split('').map((char, i) => {
        let result;
        
        if (lastSeen[char] !== undefined) {
            result = i - lastSeen[char];
        }   else {
            result = -1;
        }
        
        lastSeen[char] = i;
        
        return result;
    })
}