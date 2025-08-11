function solution(n) {
    const word = "수박"
    
    if (n % 2 !== 0) {
        return word.repeat(Math.floor(n / 2)) + "수";
    }   else {
        return word.repeat(n / 2);
    }
}