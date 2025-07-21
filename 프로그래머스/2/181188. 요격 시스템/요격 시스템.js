function solution(targets) {
    // 좌표의 끝지점을 기준으로 정렬
    targets.sort((a, b) => a[1] - b[1]);
    
    let count = 0;
    let lastOne = -Infinity;
    
    for (const [start, end] of targets) {
        // 현재 요격 위치가 start ~ end를 커버하지 못하면 새로운 lastOne 갱신
        if (!(start < lastOne && end > lastOne)) {
            lastOne = end - 0.5; // start와 end 사이에 있는 경우도 고려
            count++;
        }
    }
    
    return count;
}