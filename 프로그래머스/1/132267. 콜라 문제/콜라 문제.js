function solution(a, b, n) {
    let answer = 0;
    let bottles = n;
    
    while (bottles >= a) {
        let newCola = Math.floor(bottles / a) * b;
        
        answer += newCola;
        
        bottles = (bottles % a) + newCola;
    }
    
    return answer;
}