function solution(arr) {
    let counts = [0, 0];
    
    function compress(x, y, size) {
        const first = arr[x][y];
        let same = true;
        
        // 주어진 영역이 모두 같은 값인지 확인
        for (let i = x; i < x + size; i++) {
            for (let j = y; j < y + size; j++) {
                if (arr[i][j] !== first) {
                    same = false;
                    break;
                }
            }
            if (!same) break;
        }
        
        if (same) {
            counts[first]++;
        } else {
            const newSize = size / 2;
            compress(x, y, newSize);    // 왼쪽 위
            compress(x, y + newSize, newSize);  // 오른쪽 위
            compress(x + newSize, y, newSize);  // 왼쪽 아래
            compress(x + newSize, y + newSize, newSize);    // 오른쪽 아래
        }
    }
    
    compress(0, 0, arr.length);
    
    return counts;
}