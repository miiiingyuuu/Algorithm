function solution(s) {
    let zeroCount = 0;  // 제거된 0의 총 개수
    let transformCount = 0;  // 변환 횟수
    
    // s가 "1"이 될 때까지 반복
    while (s !== "1") {
        // 1. 현재 문자열에서 0의 개수 세기
        const currentZeros = (s.match(/0/g) || []).length;
        zeroCount += currentZeros;
        
        // 2. 모든 0을 제거하고 남은 1의 개수 구하기
        const lengthAfterRemoval = s.replace(/0/g, '').length;
        
        // 3. 남은 길이를 2진수로 변환
        s = lengthAfterRemoval.toString(2);
        
        // 4. 변환 횟수 증가
        transformCount++;
    }
    
    return [transformCount, zeroCount];
}