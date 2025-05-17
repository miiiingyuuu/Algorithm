function solution(routes) {
    // 종료 지점을 오름차순 정렬
    routes.sort((a, b) => a[1] - b[1]);
    
    let count = 0;
    let cameraPosition = -Infinity;
    
    for (let [start, end] of routes) {
        // 현재 카메라로 이 차량을 커버할 수 없다면
        if (cameraPosition < start) {
            // 새 카메라 설치
            count += 1;
            cameraPosition = end;
        }
    }
    
    return count;
}