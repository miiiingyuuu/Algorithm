function solution(k, ranges) {
    // 1. 우박수열 생성
    const collatz = [k];
    while (k !== 1) {
        k = (k % 2 === 0) ? k / 2 : k * 3 + 1;
        collatz.push(k);
    }
    
    // 2. 각 구간의 사다리꼴 넓이 계산
    const areas = [];
    for (let i = 0; i < collatz.length - 1; i++) {
        const h1 = collatz[i];
        const h2 = collatz[i + 1];
        const area = (h1 + h2) / 2;
        areas.push(area);
    }
    
    // 3. ranges에 대해 정적분 결과 계산
    const n = areas.length;
    const result = ranges.map(([a, b]) => {
        const start = a;
        const end = n + b;
        if (start > end) return -1.0;
        
        let sum = 0;
        for (let i = start; i < end; i++) {
            sum += areas[i];
        }
        return sum;
    });
    
    return result;
}