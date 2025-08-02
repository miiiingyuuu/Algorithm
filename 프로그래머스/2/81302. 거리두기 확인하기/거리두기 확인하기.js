function solution(places) {
    return places.map(place => {
        return isRoomSafe(place) ? 1 : 0;
    });
}

function isRoomSafe(place) {
    for (let r = 0; r < 5; r++) {
        for (let c = 0; c < 5; c++) {
            if (place[r][c] === 'P') {
                if (!checkAround(r, c, place)) {
                    return false;
                }
            }
        }
    }
    
    return true;
}

function checkAround(r, c, place) {
    // 상하좌우에 사람이 있는 경우
    const dr1 = [-1, 1, 0, 0];
    const dc1 = [0, 0, -1, 1];
    
    for (let i = 0; i < 4; i++) {
        const nr = r + dr1[i];
        const nc = c + dc1[i];
        if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && place[nr][nc] === 'P') {
            return false;
        }
    }
    
    // 거리가 2이지만 파티션이 있는 경우 (직선)
    const dr2 = [-2, 2, 0, 0];
    const dc2 = [0, 0, -2, 2];

    for (let i = 0; i < 4; i++) {
        const nr = r + dr2[i];
        const nc = c + dc2[i];
        
        if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && place[nr][nc] === 'P') {
            if (place[r + dr1[i]][c + dc1[i]] !== 'X') {
                return false;
            }
        }
    }
    
    // 거리가 2이지만 파티션이 없는 경우 (대각선)
    const dr3 = [-1, -1, 1, 1];
    const dc3 = [-1, 1, 1, -1];
    
    for (let i = 0; i < 4; i++) {
        const nr = r + dr3[i];
        const nc = c + dc3[i];
        
        if (nr >= 0 && nr < 5 && nc >= 0 && nc < 5 && place[nr][nc] === 'P') {
            if (place[r][nc] !== 'X' || place[nr][c] !== 'X') {
                return false;
            }
        }
    }
    
    return true;
}