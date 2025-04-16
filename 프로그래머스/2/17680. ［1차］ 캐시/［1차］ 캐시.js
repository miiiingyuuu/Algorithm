function solution(cacheSize, cities) {
    if (cacheSize === 0) {
        return cities.length * 5;
    }
    
    const cache = [];
    let totalTime = 0;
    
    for (const city of cities) {
        const lowerCity = city.toLowerCase();
        
        const cacheIndex = cache.findIndex(item => item.toLowerCase() === lowerCity);
        
        if (cacheIndex !== -1) {
            totalTime += 1;
            
            cache.splice(cacheIndex, 1);
            cache.push(lowerCity);
        } else {
            totalTime += 5;
            
            if (cache.length >= cacheSize) {
                cache.shift();
            }
            
            if (cacheSize > 0) {
                cache.push(lowerCity);
            }
        }
    }
    
    return totalTime;
}