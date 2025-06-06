function solution(arrayA, arrayB) {
    // 최대공약수(gcd) 계산 함수
    function gcd(a, b) {
        while (b !== 0) {
            let temp = b;
            b = a % b;
            a = temp;
        }
        return a
    }
    
    // 배열의 전체 gcd 계산
    function getGCDArray(arr) {
        return arr.reduce((acc, cur) => gcd(acc, cur));
    }
    
    // 어떤 수 gcd가 배열의 어떤 수도 나눌 수 없는지 확인
    function isDivisible(gcd, arr) {
        return arr.every(num => num % gcd !== 0);
    }
    
    const gcdA = getGCDArray(arrayA);
    const gcdB = getGCDArray(arrayB);
    
    let answer = 0;
    
    if (isDivisible(gcdA, arrayB)) answer = gcdA;
    if (isDivisible(gcdB, arrayA)) answer = Math.max(answer, gcdB);
    
    return answer;
}