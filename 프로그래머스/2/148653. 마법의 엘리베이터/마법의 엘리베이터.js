function solution(storey) {
    let count = 0;
    
    while (storey > 0) {
        let digit = storey % 10;
        
        if (digit > 5) {
            // 올림이 더 유리
            count += 10 - digit;
            storey = Math.floor(storey / 10) + 1;
        } else if (digit < 5) {
            // 내려가는게 유리
            count += digit;
            storey = Math.floor(storey / 10);
        } else {
            // digit이 5인 경우: 다음 자리 수를 보고 결정
            let nextDigit = Math.floor(storey / 10) % 10;
            if (nextDigit >= 5) {
                count += 5;
                storey = Math.floor(storey / 10) + 1;
            } else {
                count += 5;
                storey = Math.floor(storey / 10);
            }
        }
    }
    
    return count;
}