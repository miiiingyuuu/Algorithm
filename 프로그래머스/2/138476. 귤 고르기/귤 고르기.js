function solution(k, tangerine) {
    const sizeCount = {}
    
    for (const size of tangerine) {
        sizeCount[size] = (sizeCount[size] || 0) + 1;
    }
    
    const counts = Object.values(sizeCount).sort((a, b) => b - a)
    
    let sum = 0
    let types = 0
    
    for (const count of counts) {
        sum += count
        types++
        
        if (sum >= k) {
            break
        }
    }
    
    return types
}