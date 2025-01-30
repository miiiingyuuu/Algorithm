function solution(A,B){
    const sortedA = [...A].sort((a, b) => a - b)
    const sortedB = [...B].sort((a, b) => b - a)
    
    return sortedA.reduce((sum, val, index) => sum + (val * sortedB[index]), 0)
}