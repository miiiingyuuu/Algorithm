function solution(s) {
    const N = s.length;
    const mid = Math.floor(N / 2);
    
    if (N % 2 === 0) {
        return s[mid-1] + s[mid];
    }   else {
        return s[mid]
    }
}