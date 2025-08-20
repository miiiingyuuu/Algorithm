function solution(t, p) {
    let answer = 0;
    const pLength = p.length;
    const pNum = Number(p);
    
    for (let i = 0; i <= t.length - pLength; i++) {
        const sub = t.substring(i, i + pLength);
        if (Number(sub) <= pNum) {
            answer++;
        }
    }
    
    return answer;
}