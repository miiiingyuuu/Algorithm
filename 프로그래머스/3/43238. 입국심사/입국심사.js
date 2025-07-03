function solution(n, times) {
    let left = 1;
    let right = Math.max(...times) * n;
    let answer = right;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        // mid 시간 동안 처리 가능한 사람 수
        const people = times.reduce((acc, time) => acc + Math.floor(mid / time), 0);
        
        if (people >= n) {
            // 처리할 수 있는 사람이 더 많거나 같으면 최소 시간을 줄여보기
            answer = mid;
            right = mid - 1;
        }   else {
            // 더 많은 시간이 필요함
            left = mid + 1;
        }
    }
    
    return answer;
}