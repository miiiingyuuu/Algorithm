function solution(s, n) {
    let answer = '';
    
    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        
        if (char === ' ') {
            answer += ' ';
            continue
        }
        
        let change = s.charCodeAt(i);
        
        // 대문자
        if (change >= 65 && change <= 90) {
            change += n;
            
            if (change > 90) {
                change -= 26;
            }
        }
        
        // 대문자
        else if (change >= 97 && change <= 122) {
            change += n;
            if (change > 122) {
                change -= 26;
            }
        }
        
        answer += String.fromCharCode(change);
    }
    
    return answer;
}