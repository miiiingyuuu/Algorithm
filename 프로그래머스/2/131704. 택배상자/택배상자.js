function solution(order) {
    const stack = [];
    let current = 1;    // 컨테이너에서 꺼낼 번호
    let index = 0;      // order에서 실어야 할 상자 위치
    let count = 0;
    
    while (true) {
        // 꺼낼 상자와 order가 일치하면 바로 꺼내기
        if (current === order[index]) {
            count++;
            current++;
            index++;
        }
        
        // stack의 top과 order가 일치하면 꺼내기
        else if (stack.length > 0 && stack[stack.length - 1] === order[index]) {
            stack.pop();
            count++;
            index++;
        }
        
        // order와 현재 실어야할게 일치하지 않다면 stack에 보관
        else if (current <= order.length) {
            stack.push(current);
            current++;
        }
        
        // 위의 경우를 모두 실행할 수 없다면 끝
        else {
            break;
        }
    }
    
    return count;
}