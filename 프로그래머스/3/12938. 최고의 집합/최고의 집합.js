function solution(n, s) {
    // s 원소를 최대한 균등하게 분배하기 위해 s를 n으로 나누고 균등히 분배
    if (s < n) return [-1];
    
    const base = Math.floor(s / n);
    const reminder = s % n;
    
    const result = Array(n).fill(base);
    for (let i = 0; i < reminder; i++) {
        result[n - 1 - i] += 1;
    }
    
    return result;
}