function solution(s) {
    // 문자열 길이가 2미만 이라면 그 자체가 가장 긴 팰린드롬 수
    if (s.length < 2) {
        return s.length;
    }
    
    let answer = 1;
    
    // 중심을 기준으로 확장하여 팰린드롬 길이를 찾는 함수
    function solve(left, right) {
        // left와 right가 유효한 인덱스 범위에 있고, 두 포인터의 문자가 같은 동안 확장
        while (left >= 0 && right < s.length && s[left] === s[right]) {
            const currentLength = right - left + 1;
            answer = Math.max(answer, currentLength);
            left--;  // 왼쪽으로 한 칸 이동
            right++; // 오른쪽으로 한 칸 이동
        }
    }

    
    for (i = 0; i < s.length; i++) {
        // 문자열의 길이가 홀수인지 짝수인지에 따라 펠린드롬 수의 중앙이 달라짐
        // 1. 홀수 길이의 팰린드롬의 수일 경우 -> 같은 문자에서 출발하여 좌우 비교
        solve(i, i)
        
        // 2. 짝수 길이의 팰린드롬의 수일 경우 -> 해당 문자와 다른 오른쪽의 문자와 좌, 우를 비교
        solve(i, i+1)
    }
    
    return answer;
}