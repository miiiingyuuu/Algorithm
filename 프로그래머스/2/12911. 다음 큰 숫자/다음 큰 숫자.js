function solution(n) {
    const countOnes = (num) => {
        return num.toString(2).split('1').length - 1
    }
    
    const targetOnes = countOnes(n)
    
    let nextNum = n + 1
    while (true) {
        if (countOnes(nextNum) === targetOnes) {
            return nextNum
        }
        nextNum++
    }
    
}