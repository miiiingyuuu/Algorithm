function solution(board, skill) {
    // 효율성 검사가 있으므로 board의 최대 크기 1000 * 1000을 순회하며 하나씩 값을 주면 터질듯
    const N = board.length;
    const M = board[0].length;
    
    // 변화량을 기록할 새로운 배열
    const changes = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
    
    // 각 스킬에 대한 변화량을 changes 배열의 네 꼭짓점에 기록
    for (const s of skill) {
        const [type, r1, c1, r2, c2, degree] = s;
        const value = type === 1 ? -degree : degree;
        
        changes[r1][c1] += value;
        changes[r1][c2 + 1] -= value;
        changes[r2 + 1][c1] -= value;
        changes[r2 + 1][c2 + 1] += value;
    }
    
    // 누적합 계산 (가로, 세로)
    for (let r = 0; r <= N; r++) {
        for (let c = 1; c <= M; c++) {
            changes[r][c] += changes[r][c - 1];
        }
    }
    
    for (let c = 0; c <= M; c++) {
        for (let r = 1; r <= N; r++) {
            changes[r][c] += changes[r - 1][c];
        }
    }
    
    // 최종적으로 파괴되지 않은 건물의 수 계산
    let answer = 0;
    for (let r = 0; r < N; r++) {
        for (let c = 0; c < M; c++) {
            if (board[r][c] + changes[r][c] > 0) {
                answer++;
            }
        }
    }
    
    return answer;
}