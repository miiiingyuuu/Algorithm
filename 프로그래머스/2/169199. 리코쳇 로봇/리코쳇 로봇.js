function solution(board) {
    const n = board.length;
    const m = board[0].length;
    const map = board.map(r => r.split(""));
    
    const directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1],
    ]
    
    let start = null;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (map[i][j] === "R") start = [i, j];
        }
    }
    
    const queue = [[...start, 0]];  // x, y, 이동횟수
    const visited = Array.from({ length: n }, () => Array(m).fill(false));
    visited[start[0]][start[1]] = true;
    
    while (queue.length > 0) {
        const [x, y, count] = queue.shift();
        
        if (map[x][y] === "G") return count;
        
        for (const [dx, dy] of directions) {
            let nx = x;
            let ny = y;
            
            while (true) {
                const tx = nx + dx;
                const ty = ny + dy;
                
                if (
                    tx < 0 || tx >= n || ty < 0 || ty >= m || map[tx][ty] === "D"
                ) break;
                
                nx = tx;
                ny = ty;
            }
            
            if (!visited[nx][ny]) {
                visited[nx][ny] = true;
                queue.push([nx, ny, count + 1]);
            }
        }
    }
    
    return -1
}