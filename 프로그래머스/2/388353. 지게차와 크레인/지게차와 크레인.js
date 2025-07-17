function solution(storage, requests) {
    const n = storage.length;
    const m = storage[0].length;

    // 1. 패딩(Padding)을 추가하여 (n+2) x (m+2) 크기의 새로운 grid 생성
    // 상단 패딩
    let grid = [Array(m + 2).fill('')];
    // 중간: storage 데이터와 좌우 패딩
    for (const row of storage) {
        grid.push(['', ...row.split(''), '']);
    }
    // 하단 패딩
    grid.push(Array(m + 2).fill(''));
    
    const paddedN = n + 2;
    const paddedM = m + 2;
    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];

    // 각 요청을 순서대로 처리
    for (const request of requests) {
        const item = request[0];
        const isCrane = request.length === 2;

        // 2. 단 한 번의 BFS 탐색으로 제거할 대상을 모두 찾음
        const toRemove = new Set(); // 중복 저장을 방지하기 위해 Set 사용
        const queue = [[0, 0]]; // 항상 패딩의 (0,0)에서 탐색 시작
        const visited = Array(paddedN).fill(0).map(() => Array(paddedM).fill(false));
        visited[0][0] = true;

        let head = 0;
        while (head < queue.length) {
            const [x, y] = queue[head++];

            for (let i = 0; i < 4; i++) {
                const nx = x + dx[i];
                const ny = y + dy[i];

                // 패딩된 grid 범위 내에 있고, 아직 방문하지 않았다면
                if (nx >= 0 && nx < paddedN && ny >= 0 && ny < paddedM && !visited[nx][ny]) {
                    const neighborCell = grid[nx][ny];

                    // 3. 인접한 칸이 제거 대상(item)인지 확인
                    if (neighborCell === item) {
                        toRemove.add(`${nx},${ny}`); // 제거 목록에 추가
                    }
                    
                    // 4. 탐색을 계속 진행할지 결정
                    // 지게차: 빈 공간('')일 때만 탐색을 계속함
                    // 크레인: 모든 공간을 대상으로 탐색을 계속함
                    if (isCrane || neighborCell === '') {
                        visited[nx][ny] = true;
                        queue.push([nx, ny]);
                    }
                }
            }
        }

        // 5. 제거 목록에 있는 모든 컨테이너를 한 번에 제거
        for (const coordStr of toRemove) {
            const [x, y] = coordStr.split(',').map(Number);
            grid[x][y] = '';
        }
    }

    // 6. 패딩을 제외한 실제 창고에 남은 컨테이너 수 계산
    let answer = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            if (grid[i][j] !== '') {
                answer++;
            }
        }
    }

    return answer;
}