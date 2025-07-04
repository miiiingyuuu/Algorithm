function solution(n) {
    // 이동 경로를 저장할 배열
    const answer = [];
    
    function solve(num, from, to, aux) {
        // 옮길 원판이 하나만 남은 경우 끝
       if (num === 1) {
           answer.push([from, to]);
           return;
       }
        
        // 1. (num - 1)개의 원판을 시작 기둥(from)에서 보조 기둥(aux)으로 옮기기
        solve(num - 1, from, aux, to);
        
        // 2. 가장 큰 원판을 시작 기둥(from)에서 도착 기둥(to)으로 옮기기
        answer.push([from, to]);
        
        // 3. (num - 1)개의 원판을 보조 기둥(aux)에서 도착 기둥(to)으로 옮기기
        solve(num - 1, aux, to, from);
    }
    
    // n개의 원판을 1번에서 3번으로, 2번을 보조로 사용
    solve(n, 1, 3, 2);
    
    return answer;
}