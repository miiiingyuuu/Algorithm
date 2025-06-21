function solution(board) {
    const rows = board.length;
    const cols = board[0].length;
    let answer = 0;
    
    // DP 배열을 board 자체에 덮어쓰기하며 사용 가능
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (board[i][j] === 1 && i > 0 && j > 0) {
                board[i][j] = Math.min(
                    board[i - 1][j],
                    board[i][j - 1],
                    board[i - 1][j - 1]
                ) + 1;
            }
            answer = Math.max(answer, board[i][j]);
        }
    }

    return answer * answer; // 넓이 반환
}