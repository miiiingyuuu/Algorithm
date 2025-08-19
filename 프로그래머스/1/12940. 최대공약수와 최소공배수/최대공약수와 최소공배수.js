function solution(n, m) {
    // 최대공약수(유클리드 호제법)
    const getGCD = (a, b) => {
        while (b > 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        
        return a
    }
    
    const gcd = getGCD(n, m);
    
    // 최소공배수 -> 두 수의 곱 / 최대공약수
    const lcm = (n * m) / gcd;
    
    return [gcd, lcm];
}