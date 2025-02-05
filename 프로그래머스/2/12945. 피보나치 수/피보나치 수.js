function solution(n) {
    const MOD = 1234567
    
    if (n <= 1) return 1
    
    let prev = 0
    let curr = 1
    
    for (let i = 2; i <= n; i++) {
        const next = (prev + curr) % MOD
        prev = curr
        curr = next
    }
    
    return curr
}