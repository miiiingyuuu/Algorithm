function solution(players, m, k) {
    let count = 0;
    
    // 각 시간대(0 - 23시)에 현재 활성화된 서버의 수를 기록하는 배열
    const activeServers = Array(24).fill(0);
    
    for (let t = 0; t < 24; t++) {
        const currentPlayers = players[t];
        
        // 현재 시간대에 이용자가 없으면 서버 증대가 필요 없으므로 다음 시간으로 넘어가기
        if (currentPlayers === 0) {
            continue;
        }
        
        const requiredServers = Math.floor(currentPlayers / m);
        const currentlyActive = activeServers[t];
        
        // 필요한 서버가 이미 운영 중인 서버보다 많을 경우
        if (requiredServers > currentlyActive) {
            // 추가로 증설해야 할 서버 수
            const toAdd = requiredServers - currentlyActive;
            
            count += toAdd;
            
            // 향후 k시간 동안의 activeServers 배열을 갱신
            for (let i = 0; i < k; i++) {
                const futureHour = t + i;
                // 24시간 범위 내에서만 갱신
                if (futureHour < 24) {
                    activeServers[futureHour] += toAdd;
                }
            }
        }
    }
    
    return count;
}