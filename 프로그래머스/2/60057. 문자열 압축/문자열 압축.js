function solution(s) {
    const n = s.length;
    
    if (n === 1) {
        return 1;
    }
    
    let minLength = n;
    
    // 1개의 단위부터 n/2개 단위까지 잘라보며 압축 시도
    for (let unit = 1; unit <= Math.floor(n / 2); unit++) {
        let compressedString = "";
        let i = 0;
        
        // 현재 단위로 전체 문자열 탐색
        while (i < n) {
            const currentUnit = s.substring(i, i + unit);
            let count = 1;
            let lookaheadPos = i + unit;
            
            // 다음 단위가 현재 단위와 일치하는지 반복해서 확인
            while (lookaheadPos < n) {
                const nextUnit = s.substring(lookaheadPos, lookaheadPos + unit);
                if (currentUnit === nextUnit) {
                    count++;
                    lookaheadPos += unit;
                }   else {
                    break;
                }
            }
            
            if (count > 1) {
                compressedString += count + currentUnit;
            }   else {
                compressedString += currentUnit;
            }
            
            i = lookaheadPos;
        }
        
        minLength = Math.min(minLength, compressedString.length);
    }
    
    return minLength;
}