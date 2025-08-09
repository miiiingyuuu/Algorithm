function solution(numbers) {
    const nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    let answer = 0
    
    for (let i = 0; i < 10; i++) {
        if (numbers.includes(i)) {
            continue
        }   else {
            answer += i
        }
    }
    
    return answer
}