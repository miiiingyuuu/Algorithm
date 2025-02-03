function solution(n) {
    let count = 0;
    
    // i는 연속된 수의 개수
    for (let i = 1; i <= Math.sqrt(2 * n); i++) {
        // 등차수열의 합이 n이 되는 첫 항을 찾는 공식
        // a + (a+1) + (a+2) + ... + (a+k-1) = n
        // ka + k(k-1)/2 = n
        // a = (n - k(k-1)/2) / k
        const a = (n - (i * (i - 1) / 2)) / i;
        
        // a가 자연수인 경우만 카운트
        if (Number.isInteger(a) && a > 0) {
            count++;
        }
    }
    
    return count;
}