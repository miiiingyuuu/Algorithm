function solution(msg) {
    const dictionary = {};
    const result = [];
    
    // 길이 1인 A~Z를 사전에 등록(1~26)
    let dictSize = 1;
    for (let i = 65; i <= 90; i++) {
        dictionary[String.fromCharCode(i)] = dictSize++;
    }
    
    let i = 0;
    while (i < msg.length) {
        let w = msg[i];
        let j = i + 1;
        
        // 사전에 등록된 가장 긴 문자열 w 찾기
        while (j <= msg.length && dictionary[msg.slice(i, j)]) {
            w = msg.slice(i, j);
            j++;
        }
        
        // 사전에서 w 색인 번호 출력
        result.push(dictionary[w]);
        
        // 사전에 w+c 등록
        if (j <= msg.length) {
            const wc = msg.slice(i, j);
            dictionary[wc] = dictSize++;
        }
        
        i += w.length;
    }
    
    return result;
}