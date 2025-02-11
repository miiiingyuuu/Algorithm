function solution(arr) {
    function getGCD(a, b) {
        while (b > 0) {
            let tmp = b;
            b = a % b;
            a = tmp
        }
        return a;
    }
    
    function getLCM(a, b) {
        return (a * b) / getGCD(a, b)
    }
    
    return arr.reduce((lcm, cur) => getLCM(lcm, cur));
}