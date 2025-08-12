function solution(left, right) {
    let answer = 0;
    
    for (let i = left; i <= right; i++) {
        // 제곱근이 정수라면 약수가 홀수개, 정수가 아니라면 약수가 짝수개
        if (Number.isInteger(Math.sqrt(i))) {
            answer -= i;
        }   else {
            answer += i;
        }
    }
    
    return answer;
}