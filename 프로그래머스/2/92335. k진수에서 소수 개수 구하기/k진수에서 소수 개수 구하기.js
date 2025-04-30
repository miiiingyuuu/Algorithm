function solution(n, k) {
    const baseK = n.toString(k);
    
    const candidates = baseK.split('0');
    
    const isPrime = (num) => {
        if (num < 2) return false;
        
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    };
    
    let count = 0;
    for (let c of candidates) {
        if (c === '') continue;
        
        const num = Number(c);
        if (isPrime(num)) count++;
    }
    
    return count;
}