function solution(n, k) {
    let answer = [];
    let numbers = Array.from({ length: n }, (_, i) => i + 1);
    let factorial = [1];
    
    //  팩토리얼 미리 계산
    for (let i = 1; i <= n; i++) {
        factorial[i] = factorial[i - 1] * i;
    }
    
    k--; // 0-based index로 변경
    
    for (let i = n; i > 0; i--) {
        let f = factorial[i - 1];
        let index = Math.floor(k / f);
        answer.push(numbers[index]);
        numbers.splice(index, 1);
        k %= f;
    }
    
    return answer;
}