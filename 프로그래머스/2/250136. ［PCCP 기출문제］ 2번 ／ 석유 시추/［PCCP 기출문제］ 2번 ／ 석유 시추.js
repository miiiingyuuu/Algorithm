function solution(land) {
    const n = land.length;
    const m = land[0].length;
    
    const clusterSizes = {};
    let clusterId = 2;
    
    const dr = [-1, 1, 0, 0];
    const dc = [0, 0, -1, 1];
    
    // 모든 석유 덩어리를 찾아 ID를 부여하고 크기를 계산
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < m; c++) {
            if (land[r][c] === 1) {
                const queue = [[r, c]];
                land[r][c] = clusterId;
                let currentSize = 0;
                
                let head = 0;
                while (head < queue.length) {
                    const [cr, cc] = queue[head++];
                    currentSize++;
                    
                    for (let i = 0 ; i < 4; i++) {
                        const nr = cr + dr[i];
                        const nc = cc + dc[i];
                        
                        if (nr >= 0 && nr < n && nc >= 0 && nc < m && land[nr][nc] === 1) {
                            land[nr][nc] = clusterId;
                            queue.push([nr, nc]);
                        }
                    }
                }
                
                clusterSizes[clusterId] = currentSize;
                clusterId++;
            }
        }
    }
    
    // 각 열에서 얻을 수 있는 총 석유량 계산
    const oilPerColumn = new Array(m).fill(0);
    for (let c = 0; c < m; c++) {
        const clustersInThisColumn = new Set();
        
        for (let r = 0; r < n; r++) {
            if (land[r][c] > 1) {
                clustersInThisColumn.add(land[r][c]);
            }
        }
        
        // 이 열과 연결된 모든 덩어리의 크기를 합산
        let totalOilForColumn = 0;
        for (const id of clustersInThisColumn) {
            totalOilForColumn += clusterSizes[id];
        }
        oilPerColumn[c] = totalOilForColumn;
    }
    
    // 계산된 모든 열의 석유량 중 최대값 변환
    return Math.max(0, ...oilPerColumn);
}