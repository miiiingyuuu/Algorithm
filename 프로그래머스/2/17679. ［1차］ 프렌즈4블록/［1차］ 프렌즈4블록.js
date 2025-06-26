function solution(m, n, board) {
    let newBoard = board.map(row => row.split(''));
    let count = 0;
    
    while (true) {
        let toDelete = [];
        
        // 1. 터뜨릴 블록 찾기
        for (let i = 0; i < m - 1; i++) {
            for (let j = 0; j < n - 1; j++) {
                if (newBoard[i][j] &&
                    newBoard[i][j] === newBoard[i][j + 1] &&
                    newBoard[i][j] === newBoard[i + 1][j] &&
                    newBoard[i][j] === newBoard[i + 1][j + 1]) {
                    toDelete.push([i, j])
                }
            }
        }
        
        // 더 이상 터뜨릴 블록이 없으면 종료
        if (toDelete.length === 0) {
            break;
        }
        
        // 2. 찾은 블록 터뜨리기 (0으로 만들기)
        toDelete.forEach(([row, col]) => {
            if (newBoard[row][col]) {
                newBoard[row][col] = 0;
                count++;
            }
            if (newBoard[row][col + 1]) {
                newBoard[row][col + 1] = 0;
                count++;
            }
            if (newBoard[row + 1][col]) {
                newBoard[row + 1][col] = 0;
                count++;
            }
            if (newBoard[row + 1][col + 1]) {
                newBoard[row + 1][col + 1] = 0;
                count++;
            }
        });
        
        // 3. 블록 아래로 떨어뜨리기
        for (let j = 0; j < n; j++) {
            let column = [];
            for (let i = m - 1; i >= 0; i--) {
                if (newBoard[i][j]) {
                    column.push(newBoard[i][j]);
                }
            }
            for (let i = m - 1; i >= 0; i--) {
                newBoard[i][j] = column.shift() || 0;
            }
        }
    }
    
    return count;
}