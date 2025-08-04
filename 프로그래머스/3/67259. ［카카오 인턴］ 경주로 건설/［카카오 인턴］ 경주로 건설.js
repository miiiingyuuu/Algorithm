function solution(board) {
    const N = board.length;
    
    // 0: 상, 1: 우, 2: 하, 3: 좌
    const dr = [-1, 0, 1, 0];
    const dc = [0, 1, 0, -1];
    
    // [r][c][direction]
    const costs = Array.from({ length: N }, () => 
         Array.from({ length: N }, () => Array(4).fill(Infinity))
    );
    
    const queue = [];
    
    // 큐의 시작점을 처리하기 위한 포인터 사용
    let head = 0;

    // 오른쪽으로 가는 경우
    if (board[0][1] === 0) {
        costs[0][1][1] = 100;
        queue.push([0, 1, 1, 100]);
    }

    // 아래로 가는 경우
    if (board[1][0] === 0) {
        costs[1][0][2]
        queue.push([1, 0, 2, 100]);
    }

    while (head < queue.length) {
        const [r, c, prevDir, cost] = queue[head++];
        
        for (let nextDir = 0; nextDir < 4; nextDir++) {
            const nr = r + dr[nextDir];
            const nc = c + dc[nextDir];
            
            if (nr < 0 || nr >= N || nc < 0 || nc >= N || board[nr][nc] === 1) {
                continue;
            }
            
            const newCost = cost + 100 + (prevDir === nextDir ? 0 : 500);
            
            // 새로운 경로의 비용이 기존 비용보다 작거나 같을 경우에만 갱신하고 탐색 계속
            if (newCost < costs[nr][nc][nextDir]) {
                costs[nr][nc][nextDir] = newCost;
                queue.push([nr, nc, nextDir, newCost]);
            }
        }
    }
    
    return Math.min(...costs[N-1][N-1]);
}