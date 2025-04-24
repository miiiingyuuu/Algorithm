function solution(str1, str2) {
    const makeMultiSet = (str) => {
        const result = [];
        str = str.toLowerCase();
        for (let i = 0; i < str.length - 1; i++) {
            const pair = str[i] + str[i + 1];
            if (pair.match(/^[a-z]{2}$/)) {
                result.push(pair);
            }
        }
        return result
    };
    
    const arr1 = makeMultiSet(str1);
    const arr2 = makeMultiSet(str2);
    
    const map1 = new Map();
    const map2 = new Map();
    
    for (let el of arr1) map1.set(el, (map1.get(el) || 0) + 1);
    for (let el of arr2) map2.set(el, (map2.get(el) || 0) + 1);
    
    let intersection = 0;
    let union = 0;
    
    const allKeys = new Set([...map1.keys(), ...map2.keys()]);
    for (let key of allKeys) {
        const count1 = map1.get(key) || 0;
        const count2 = map2.get(key) || 0;
        intersection += Math.min(count1, count2);
        union += Math.max(count1, count2);
    }
    
    const ans = union === 0 ? 1 : intersection / union;
    
    return Math.floor(ans * 65536);
}