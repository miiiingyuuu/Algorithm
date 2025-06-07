function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    const grid = maps.map(row => row.split(''));

    let start, lever;

    // 시작점(S), 레버(L), 출구(E) 위치 탐색
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (grid[i][j] === 'S') start = [i, j];
            if (grid[i][j] === 'L') lever = [i, j];
        }
    }

    // 두 구간을 각각 BFS로 최단 거리 탐색
    const toLever = bfs(start, 'L', maps);
    const toExit = bfs(lever, 'E', maps);

    return toLever === -1 || toExit === -1 ? -1 : toLever + toExit;
}

function bfs(start, targetChar, maps) {
    const n = maps.length;
    const m = maps[0].length;
    const grid = maps.map(row => row.split('')); // 새로 복사

    const visited = Array.from({ length: n }, () => Array(m).fill(false));
    const queue = [start];
    visited[start[0]][start[1]] = true;

    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    let time = 0;

    while (queue.length) {
        let size = queue.length;
        for (let i = 0; i < size; i++) {
            const [x, y] = queue.shift();

            if (grid[x][y] === targetChar) {
                return time;
            }

            for (let d = 0; d < 4; d++) {
                const nx = x + dx[d];
                const ny = y + dy[d];

                if (
                    nx >= 0 && nx < n &&
                    ny >= 0 && ny < m &&
                    grid[nx][ny] !== 'X' &&
                    !visited[nx][ny]
                ) {
                    visited[nx][ny] = true;
                    queue.push([nx, ny]);
                }
            }
        }
        time++;
    }

    return -1; // targetChar에 도달하지 못함
}
