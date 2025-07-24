function solution(name) {
    const n = name.length;
    let verticalMoves = 0;
    
    // 위, 아래 움직임 계산
    for (let i = 0; i < n; i++) {
        const diff = name.charCodeAt(i) - 'A'.charCodeAt(0);
        verticalMoves += Math.min(diff, 26 - diff);
    }
    
    let horizontalMoves = n-1;
    
    // 좌, 우 움직임 계산
    for (let i = 0; i < n; i++) {
        let nextIndex = i + 1;
        // A가 아닌 문자를 찾기
        while (nextIndex < n && name[nextIndex] === 'A') {
            nextIndex++;
        }
        
        // 만약 끝까지 갔다면 모두 A라는 뜻이므로 시작점에서 i로 이동만 하면 됨
        if (nextIndex === n) {
            horizontalMoves = Math.min(horizontalMoves, i);
            break;
        }
        
        // 오른쪽으로 갔다가 왼쪽으로 가는 경우
        const moveRightThenLeft = i + i + (n - nextIndex);
        
        // 왼쪽으로 갔다가 오른쪽으로 가는 경우
        const moveLeftThenRight = (n - nextIndex) * 2 + i;
        
        horizontalMoves = Math.min(horizontalMoves, moveRightThenLeft, moveLeftThenRight);
    }
    
    return verticalMoves + horizontalMoves;
}