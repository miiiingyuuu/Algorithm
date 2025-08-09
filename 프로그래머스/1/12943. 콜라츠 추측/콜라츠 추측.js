function solution(num) {
    for (let i = 0; i < 501; i++) {
        if (num === 1) {
            return i
        }
        
        if (num % 2 === 0) {
            num /= 2
        }   else {
            num *= 3
            num += 1
        }
    }
    
    return -1
}