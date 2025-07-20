function solution(board) {
    // O, X 개수 세기
    let oCount = 0;
    let xCount = 0;
    board.forEach(row => {
        for (let cell of row) {
            if (cell === 'O') oCount++;
            else if (cell === 'X') xCount++;
        }
    });
    
    function isWin(player) {
        for (let i = 0; i < 3; i++) {
            // 가로, 세로
            if (
                board[i][0] === player &&
                board[i][1] === player &&
                board[i][2] === player
            )   return true;
            
            if (
                board[0][i] === player &&
                board[1][i] === player &&
                board[2][i] === player
            )   return true;
        }
        
        // 대각선
        if (
            board[0][0] === player &&
            board[1][1] === player &&
            board[2][2] === player
        )   return true;
        if (
            board[0][2] === player &&
            board[1][1] === player &&
            board[2][0] === player
        )   return true;
        
        // 위의 경우가 모두 해당되지 않다면
        return false;
    }
    
    const oWin = isWin('O');
    const xWin = isWin('X');
    
    // 잘못된 턴 수
    if (xCount > oCount) return 0;
    if (oCount - xCount > 1) return 0;
    
    // 승리자가 있지만 턴 수가 맞지 않은 경우
    if (oWin && oCount !== xCount + 1) return 0;
    if (xWin && oCount !== xCount) return 0;
    
    // 동시에 둘 다 승리하는 경우는 불가능
    if (oWin && xWin) return 0;
    
    return 1;
}