function solution(n) {
    let battery = 0
    
    while (n > 0) {
        if (n % 2 === 1) {
            battery++
            n -= 1
        }
        
        n = n / 2
    }
    return battery
}