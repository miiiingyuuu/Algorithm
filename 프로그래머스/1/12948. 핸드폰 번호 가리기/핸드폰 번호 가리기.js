function solution(phone_number) {
    const N = phone_number.length;
    let count = 0
    
    let answer = ""
    
    for (let i = N - 1; i >= 0; i--) {
        if (count < 4) {
            answer += phone_number[i]
            count += 1
        }   else {
            answer += '*'
        }
    }
    
    const reverseAnswer = answer.split("").reverse().join("");
    
    return reverseAnswer
}