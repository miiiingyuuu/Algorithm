function solution(numbers) {
    const digits = numbers.split("");
    const numSet = new Set();
    
    // 모든 순열을 생성
    function generatePermutations(arr, prefix = "") {
        if (prefix.length > 0) {
            numSet.add(Number(prefix));
        }
        for (let i = 0; i < arr.length; i++) {
            const rest = arr.slice(0, i).concat(arr.slice(i + 1));
            generatePermutations(rest, prefix + arr[i]);
        }
    }
    
    generatePermutations(digits);
    
    // 소수 판별 함수
    function isPrime(n) {
        if (n < 2) return false;
        for (let i = 2; i * i <= n; i++) {
            if (n % i === 0) return false;
        }
        return true;
    }
    
    // Set에 있는 숫자들 중 소수 개수 세기
    let count = 0;
    for (let num of numSet) {
        if (isPrime(num)) {
            count++;
        }
    }
    
    return count;
}