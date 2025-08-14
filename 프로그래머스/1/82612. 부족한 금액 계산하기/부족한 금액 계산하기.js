function solution(price, money, count) {
    let answer = 0;
    let moneyNeed = 0;
    
    for (let i = 1; i <= count; i++) {
        moneyNeed += price * i
    }
    
    answer = moneyNeed - money
    
    return answer > 0 ? answer : 0
}