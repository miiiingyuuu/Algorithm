function solution(a) {
    // 풍선이 2개 이하면 모두 생존 가능
    if (a.length <= 2) {
        return a.length;
    }
    
    const n = a.length;
    
    // 왼쪽부터 그룹을 했을 때의 최소값이 나오는 경우 저장
    const leftMin = new Array(n);
    leftMin[0] = a[0];
    for (let i = 1; i < n; i++) {
        leftMin[i] = Math.min(leftMin[i - 1], a[i]);
    }
    
    // 오른쪽부터 그룹을 했을 때의 최소값이 나오는 경우 저장
    const rightMin = new Array(n);
    rightMin[n - 1] = a[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        rightMin[i] = Math.min(rightMin[i + 1], a[i]);
    }
    
    let answer = 0;
    for (let i = 0; i < n; i++) {
        // 가장 왼쪽 풍선은 왼쪽 그룹이 없으므로 항상 생존이 가능
        if (i === 0) {
            answer++;
            continue;
        }
        
        // 가장 오른쪽 풍선은 오른쪽 그룹이 없으므로 항상 생존이 가능
        if (i === n - 1) {
            answer++;
            continue;
        }
        
        // 현재 풍선이 왼쪽 그룹의 최소값보다 작거나, 오른쪽 그룹의 최소값보다 작으면 생존 가능
        const minLeftOfI = leftMin[i - 1];
        const minRightOfI = rightMin[i + 1];
        
        if (a[i] < minLeftOfI || a[i] < minRightOfI) {
            answer++;
        }
    }
    
    return answer;
}