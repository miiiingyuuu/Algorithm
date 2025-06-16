function solution(rows, columns, queries) {
    const board = Array.from({ length: rows }, (_, i) => 
        Array.from({ length: columns }, (_, j) => i * columns + j + 1));
    
    const result = [];
    
    for (const [x1, y1, x2, y2] of queries) {
        const minValue = rotate(board, x1 - 1, y1 - 1, x2 - 1, y2 - 1);
        result.push(minValue)
    }
    
    return result;
}

function rotate(board, x1, y1, x2, y2) {
    const temp = board[x1][y1];
    let minValue = temp;
    
    // 왼 -> 위
    for (let i = x1; i < x2; i++) {
        board[i][y1] = board[i+1][y1];
        minValue = Math.min(minValue, board[i][y1]);
    }
    
    // 아래 -> 왼
    for (let i = y1; i < y2; i++) {
        board[x2][i] = board[x2][i+1];
        minValue = Math.min(minValue, board[x2][i]);
    }
    
    // 오 -> 아래
    for (let i = x2; i > x1; i--) {
        board[i][y2] = board[i-1][y2];
        minValue = Math.min(minValue, board[i][y2]);
    }
    
    // 위 -> 오른
    for (let i = y2; i > y1; i--) {
        board[x1][i] = board[x1][i-1];
        minValue = Math.min(minValue, board[x1][i]);
    }
    
    board[x1][y1+1] = temp;
    
    return minValue;
}