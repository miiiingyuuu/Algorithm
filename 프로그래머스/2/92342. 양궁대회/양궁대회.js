function solution(n, info) {
    let maxDiff = 0;
    let answer = [-1];
    
    function dfs(index, arrowsLeft, ryanShots) {
        // 모든 과녁을 다 확인했거나, 화살을 다 쏜 경우
        if (index > 10 || arrowsLeft <= 0) {
            const finalRyanShots = [...ryanShots];
            if (arrowsLeft > 0) {
                finalRyanShots[10] += arrowsLeft;
            }
            
            // 점수 계산
            let ryanScore = 0;
            let apeachScore = 0;
            
            for (let i = 0; i <= 10; i++) {
                if (finalRyanShots[i] > info[i]) {
                    ryanScore += (10 - i);
                }   else if (info[i] > 0) {
                    apeachScore += (10 - i);
                }
            }
            
            const diff = ryanScore - apeachScore;
            
            // 라이언이 이겼고, 기존 최대 점수차보다 크거나 같은 경우
            if (diff > 0 && diff >= maxDiff) {
                // 새로운 최대 점수차인 경우
                if (diff > maxDiff) {
                    maxDiff = diff;
                    answer = finalRyanShots;
                }   else {
                    // 점수차가 같은 경우, 낮은 점수를 더 많이 맞힌 경우로 갱신
                    for (let i = 10; i >= 0; i--) {
                        if (finalRyanShots[i] > answer[i]) {
                            answer = finalRyanShots;
                            return;
                        }
                        if (finalRyanShots[i] < answer[i]) {
                            return;
                        }
                    }
                }
            }
            
            return;
        }
        
        // 1. 현재 과녁의 점수를 얻는 경우
        const arrowsToWin = info[index] + 1;
        if (arrowsLeft >= arrowsToWin) {
            const nextRyanShots = [...ryanShots];
            nextRyanShots[index] = arrowsToWin;
            dfs(index + 1, arrowsLeft - arrowsToWin, nextRyanShots);
        }

        // 2. 현재 과녁의 점수를 포기하는 경우
        dfs(index + 1, arrowsLeft, ryanShots);
    }
    
    dfs(0, n, Array(11).fill(0));
    
    return answer;
}