function solution(n) {
    let answer = "";
    
    while (n > 0) {
        let remainder = n % 3;
        n = Math.floor(n / 3);
        
        if (remainder === 0) {
            answer = "4" + answer;
            n -= 1;
        }   else if (remainder === 1) {
            answer = "1" + answer;
        }   else if (remainder === 2) {
            answer = "2" + answer;
        }
    }
    
    return answer
}