function solution(n) {
    // 아래로 이동, 오른쪽으로 이동, 왼쪽 위로 이동
    const triangle = Array.from({ length: n }, (_, i) => Array(i + 1).fill(0));
    let num = 1;
    let x = -1, y = 0; // 시작 위치
    let dir = 0; // 방향: 0 = down, 1 = right, 2 = up-left
    
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            if (dir % 3 === 0) x++;
            else if (dir % 3 === 1) y++;
            else { x--; y--; }
            triangle[x][y] = num++;
        }
        dir++;
    }
    
    return triangle.flat();
}