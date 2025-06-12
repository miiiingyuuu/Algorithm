function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const visited = Array.from({ length: n }, () => Array(m).fill(false));
    const directions = [
        [-1, 0],
        [0, 1],
        [1, 0],
        [0, -1]
    ]
    const result = [];
    
    const solve = (x, y) => {
        let queue = [[x, y]];
        visited[x][y] = true;
        let sum = parseInt(maps[x][y]);
        
        while (queue.length > 0) {
            const [curX, curY] = queue.shift();
            
            for (const [dx, dy] of directions) {
                const nx = curX + dx;
                const ny = curY + dy;
                
                if (
                    nx >= 0 && nx < n && 
                    ny >= 0 && ny < m && 
                    !visited[nx][ny] &&
                    maps[nx][ny] !== 'X'
                ) {
                    visited[nx][ny] = true;
                    sum += parseInt(maps[nx][ny]);
                    queue.push([nx, ny]);
                }
            }
        }
        
        return sum;
    }
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (!visited[i][j] && maps[i][j] !== 'X') {
                result.push(solve(i, j));
            }
        }
    }
    
    return result.length === 0 ? [-1] : result.sort((a, b) => a - b);
}