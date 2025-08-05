function solution(relation) {
    const colCount = relation[0].length;
    const rowCount = relation.length;
    const uniqueKeys = [];
    
    // 모든 속성 조합에 대해 반복
    for (let i = 1; i < (1 << colCount); i++) {
        // 유일성 검사
        const keySet = new Set();
        for (let j = 0; j < rowCount; j++) {
            let key = '';
            // 현재 조합에 해당하는 컬럼들의 데이터를 합쳐 key 생성
            for (let k = 0; k < colCount; k++) {
                if ((i >> k) & 1) {
                    key += relation[j][k] + '-';
                }
            }
            keySet.add(key);
        }
        
        if (keySet.size === rowCount) {
            uniqueKeys.push(i);
        }
    }
    
    // 최소성 검사
    const candidateKeys = [];
    while (uniqueKeys.length > 0) {
        // 가장 작은 조합부터 꺼내기
        const key = uniqueKeys.shift();
        candidateKeys.push(key);
        
        for (let i = uniqueKeys.length - 1; i >= 0; i--) {
            if ((uniqueKeys[i] & key) === key) {
                uniqueKeys.splice(i, 1);
            }
        }
    }
    
    return candidateKeys.length;
}