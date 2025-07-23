function solution(cards) {
    const n = cards.length;
    const visited = new Array(n).fill(false);
    const groupSizes = [];
    
    // 0번째 상자부터 순서대로 확인
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            let count = 0;
            let currentIndex = i;
            
            // 이미 방문한 상자를 만날 때까지 계속 상자 열기
            while (!visited[currentIndex]) {
                visited[currentIndex] = true;
                count++;
                
                currentIndex = cards[currentIndex] - 1;
            }
            // 탐색이 끝난 그룹의 크기를 저장
            groupSizes.push(count);
        }
    }
    
    // 그룹이 하나뿐이라면 점수는 0점
    if (groupSizes.length < 2) {
        return 0;
    }
    
    // 내림차순으로 정렬하여 가장 큰 두 그룹 찾기
    groupSizes.sort((a, b) => b - a);
    
    // 가장 큰 두그룹의 크기를 곱하여 최고 점수 반환
    return groupSizes[0] * groupSizes[1];
}