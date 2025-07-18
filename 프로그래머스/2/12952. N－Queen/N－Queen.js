function solution(n) {
    let count = 0;
    const board = Array(n).fill(0);
    
    function isSafe(row, col) {
        for (let i = 0; i < row; i++) {
            // 같은 열에 있거나, 대각선에 있는 경우 x
            if (board[i] === col || Math.abs(board[i] - col) === row - i) {
                return false;
            }
        }
        
        return true;
    }
    
    function solve(row) {
        if (row === n) {
            count++;
            return
        }
        
        for (let col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row] = col;
                solve(row + 1);
            }
        }
    }
    
    solve(0)
    return count;
}