function solution(n) {
    const to3 = n.toString(3);
    
    const reversed = to3.split('').reverse().join('');
    
    const answer = parseInt(reversed, 3);
    
    return answer;
}