function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const dx = [-1, 0, 1, 0];
    const dy = [0 ,1, 0, -1];
    
    const visited = Array.from({ length: n }, () => Array(m).fill(0));
    const q = [[0, 0]];
    visited[0][0] = 1;
    
    while (q.length) {
        const [x, y] = q.shift();
        
        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];
            
            if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
            
            if (maps[nx][ny] === 0 || visited[nx][ny] !== 0) continue;
            
            visited[nx][ny] = visited[x][y] + 1;
            q.push([nx, ny]);
        }
    }
    
    return visited[n-1][m-1] === 0 ? -1 : visited[n-1][m-1]
}