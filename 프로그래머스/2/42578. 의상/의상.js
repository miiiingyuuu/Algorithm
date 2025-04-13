function solution(clothes) {
    const clothesMap = {};
    
    for (const [name, type] of clothes) {
        if (!clothesMap[type]) {
            clothesMap[type] = 0;
        }
        clothesMap[type]++;
    }
    
    let result = 1;
    for (const type in clothesMap) {
        result *= (clothesMap[type] + 1);
    }
    
    return result - 1;
}