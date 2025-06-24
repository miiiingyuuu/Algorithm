function solution(files) {
    // 파일명을 HEAD와 NUMBER로 분리하기 위한 정규 표현식
    const re = /(\D+)(\d+)/;
    
    return files.sort((a, b) => {
        // a, b 파일 명을 각각 HEAD와 NUMBER로 분리
        const [, headA, numberA] = a.match(re);
        const [, headB, numberB] = b.match(re);
        
        // 1. HEAD 부분을 대소문자 구분 없이 비교
        const lowerHeadA = headA.toLowerCase();
        const lowerHeadB = headB.toLowerCase();
        
        if (lowerHeadA < lowerHeadB) {
            return -1;
        }
        if (lowerHeadA > lowerHeadB) {
            return 1;
        }
        
        // 2. HEAD 부분이 같다면 NUMBER 부분을 숫자 크기로 비교
        const numA = parseInt(numberA, 10);
        const numB = parseInt(numberB, 10);
        
        // 숫자 차이를 반환하여 정렬 (오름차순)
        return numA - numB;
    });
}