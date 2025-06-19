function solution(data, col, row_begin, row_end) {
    // 1. col 번째 컬럼 기준 오름차순 정렬, 동일하면 첫 번째 컬럼 기준 내림차순 정렬
    data.sort((a, b) => {
        if (a[col - 1] === b[col - 1]) {
            return b[0] - a[0];
        }
        return a[col - 1] - b[col - 1];
    });
    
    // 2. row_begin ~ row_end까지 계산 후 XOR 누적
    let result = 0;
    for (let i = row_begin - 1; i <= row_end - 1; i++) {
        const row = data[i];
        let s_i = row.reduce((sum, val) => sum + (val % (i + 1)), 0);
        result ^= s_i;
    }
    
    return result;
}