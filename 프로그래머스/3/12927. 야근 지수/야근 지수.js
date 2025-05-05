function solution(n, works) {
    // 일의 작업량이 없으면 0
    if (works.reduce((a, b) => a + b, 0) <= n) return 0;
    
    // 내림차순 정렬
    works.sort((a, b) => b - a);
    
    for (let i = 0; i < n; i++) {
        works[0] -= 1;
        
        let j = 0;
        while (j + 1 < works.length && works[j] < works[j+1]) {
            [works[j], works[j+1]] = [works[j+1], works[j]];
            j++;
        }
    }
    
    return works.reduce((sum, w) => sum + w * w, 0);
}