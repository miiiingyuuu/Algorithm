function getBlockNumber(num) {
    // 1번 위치에는 블록을 놓을 수 없으므로 0을 반환
    if (num === 1) {
        return 0;
    }
    
    // num이 소수인 경우를 대비해 가장 큰 약수를 1로 초기화
    let maxDivisor = 1;
    
    // 2부터 숫자의 제곱근까지만 반복하여 약수 찾기
    for (let i = 2; i * i <= num; i++) {
        // i가 num의 약수인지 확인
        if (num % i === 0) {
            if (num / i <= 10000000) {
                return num / i;
            }
            
            maxDivisor = i;
        }
    }
    
    return maxDivisor;
}

function solution(begin, end) {
    const answer = [];
    
    // begin부터 end까지 각 위치에 대해 블록 번호를 계산
    for (let i = begin; i <= end; i++) {
        answer.push(getBlockNumber(i));
    }
    
    return answer;
}