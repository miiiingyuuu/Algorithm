function solution(sizes) {
    let maxH = 0;
    let maxW = 0;
    
    for (const size of sizes) {
        const w = Math.max(size[0], size[1]);
        const h = Math.min(size[0], size[1]);
        
        maxH = Math.max(maxH, h);
        maxW = Math.max(maxW, w);
    }
    
    return maxH * maxW;
}