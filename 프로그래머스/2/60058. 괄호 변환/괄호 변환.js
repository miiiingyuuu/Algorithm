function isCorrect(s) {
    let stack = 0;
    for (const char of s) {
        if (char === '(') {
            stack++;
        }   else {
            stack--;
        }
        
        if (stack < 0) {
            return false;
        }
    }
    
    return stack === 0;
}

function solution(p) {
    if (p === "") {
        return "";
    }
    
    let balance = 0;
    let u = "";
    let v = "";
    for (let i = 0; i < p.length; i++) {
        if (p[i] === '(') {
            balance++;
        }   else {
            balance--;
        }
        
        // balance가 0이 되는 지점이 가장 작은 단위의 균형잡힌 괄호 문자열
        if (balance === 0) {
            u = p.substring(0, i+1);
            v = p.substring(i+1);
            break;
        }
    }
    
    if (isCorrect(u)) {
        return u + solution(v);
    }
    else {
        let answer = '(';
        answer += solution(v);
        answer += ')';
        
        const middleU = u.slice(1, -1);
        for (const char of middleU) {
            answer += char === '(' ? ')' : '(';
        }
        
        return answer;
    }
}