function solution(x, y, n) {
    const visited = new Set();
    const queue = [[x, 0]] // [현재 값, 연산 횟수]
    let index = 0;
    
    while (index < queue.length) {
        const [current, count] = queue[index++];
        
        // y에 도달하면 count 반환
        if (current === y) return count;
        
        // 방문 여부 확인
        if (visited.has(current)) continue;
        visited.add(current);
        
        // n을 더하기, *2, *3 하는 경우
        const nexts = [current + n, current * 2, current * 3];
        for (const next of nexts) {
            if (next <= y && !visited.has(next)) {
                queue.push([next, count + 1]);
            }
        }
    }
    
    return -1;
}