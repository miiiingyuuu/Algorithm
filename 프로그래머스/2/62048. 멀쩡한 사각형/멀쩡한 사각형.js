function solution(w, h) {
    // 최대공약수(GCD)를 구하는 함수(유클리드 호제법)
    const getGCD = (a, b) => {
        // b가 0이 될 때까지 반복하며, a를 b로 나눈 나머지를 새로운 b로 사용
        while (b > 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    };
    
    // W와 H의 최대공약수 구하기
    const gcd = getGCD(w, h);
    
    // w * h 계산 시 Number 타입 한계를 넘을 수 있으므로 BigInt 사용
    const totalSquares = BigInt(w) * BigInt(h);
    
    // 사용할 수 없는 사각형의 개수: w + h - 최대공약수
    const unusableSquares = BigInt(w) + BigInt(h) - BigInt(gcd);
    
    const answer = totalSquares - unusableSquares;
    
    return answer;
}