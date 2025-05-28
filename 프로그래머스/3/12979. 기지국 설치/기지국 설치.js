function solution(n, stations, w) {
    // n: 아파트 개수, stations: 현재 기지국 설치된 곳, w: 전파 도달 거리
    let answer = 0;
    let coverage = 2 * w + 1
    let position = 1;
    
    for (let i = 0; i < stations.length; i++) {
        const left = stations[i] - w;
        const right = stations[i] + w;
        
        // 커버되지 않는 영역이 있다면
        if (position < left) {
            const uncovered = left - position;
            answer += Math.ceil(uncovered / coverage);            
        }
        // 다음 체크할 시작 위치
        position = right + 1;
    }
    
    // 마지막 기지국 이후 커버되지 않은 영역
    if (position <= n) {
        const uncovered = n - position + 1;
        answer += Math.ceil(uncovered / coverage);
    }
    
    return answer;
}