function solution(expression) {
    // 모든 연산자 우선순위 조합을 정의
    const priorities = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ];
    
    let answer = 0;
    
    // 정규식을 사용하여 표현식 숫자와 연산자로 나누기
    const initialNumbers = expression.split(/\D/).map(Number);
    const initialOperators = expression.replace(/[0-9]/g, '').split('');
    
    // 우선순위 조합으로 순회
    for (const priority of priorities) {
        const numbers = [...initialNumbers];
        const operators = [...initialOperators];
        
        // 현재 우선순위의 연산자가 더 이상 없을때까지 반복
        for (const op of priority) {
            while (operators.includes(op)) {
                const index = operators.indexOf(op);
                
                let result;
                if (op === '*') {
                    result = numbers[index] * numbers[index + 1];
                }   else if (op === '+') {
                    result = numbers[index] + numbers[index + 1];
                }   else if (op === '-') {
                    result = numbers[index] - numbers[index + 1];
                }
                
                // 계산된 숫자 2개와 연산자 제거 후 그 위치에 연산값 넣기
                numbers.splice(index, 2, result);
                operators.splice(index, 1);
            }
        }
        
        answer = Math.max(answer, Math.abs(numbers[0]));
    }
    
    return answer;
}