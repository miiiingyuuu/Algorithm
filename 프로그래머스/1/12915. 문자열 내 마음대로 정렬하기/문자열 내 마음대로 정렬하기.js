function solution(strings, n) {
    strings.sort((a, b) => {
        const charA = a.charAt(n);
        const charB = b.charAt(n);
        
        if (charA === charB) {
            // 해당 인덱스의 문자가 같으면 사전순으로 정렬
            return a.localeCompare(b);
        }   else {
            // 인덱스 n의 문자를 기준으로 오름차순 정렬
            return charA.localeCompare(charB);
        }
    });
    
    return strings;
}