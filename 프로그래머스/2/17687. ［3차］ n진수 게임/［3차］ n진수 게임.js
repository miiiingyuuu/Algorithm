function solution(n, t, m, p) {
    let result = '';
    let number = 0;
    let gameStr = '';
    
    while (gameStr.length < t * m) {
        gameStr += number.toString(n).toUpperCase();
        number++;
    }
    
    for (let i = 0; result.length < t; i++) {
        if (i % m === p - 1) {
            result += gameStr[i];
        }
    }
    
    return result;
}