function solution(diffs, times, limit) {
    let answer = 0;
    let left = 1;
    let right = 100001
    
    while (left <= right) {
        // js에서는 큰 숫자를 다룰 때 BigInt를 사용하는 것이 안정적
        const mid = Math.floor((left + right) / 2);
        let totalTime = 0n;
        
        for (let i = 0; i < diffs.length; i++) {
            const diff = diffs[i];
            const time_cur = BigInt(times[i]);
            
            if (diff <= mid) {
                totalTime += time_cur;
            }   else {
                // 첫 번째 퍼즐은 항상 1이므로 diff <= mid임 따라서 i > 0 일때만 time_prev가 의미가 있음
                const time_prev = BigInt(times[i - 1]);
                const mistakes = BigInt(diff - mid);
                
                totalTime += (time_cur + time_prev) * mistakes + time_cur;
            }
        }
        
        if (totalTime <= BigInt(limit)) {
            // 현재 숙련도로 시간 내에 해결이 가능하므로, 더 낮은 숙련도로 가능한지 탐색
            answer = mid;
            right = mid - 1;
        }   else {
            left = mid + 1;
        }
    }
    
    return answer;
}