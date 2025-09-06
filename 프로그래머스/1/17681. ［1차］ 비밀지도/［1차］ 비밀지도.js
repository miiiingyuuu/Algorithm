function solution(n, arr1, arr2) {
    const result = [];
    
    for (let i = 0; i < n; i++) {
        // arr1과 arr2의 각 요소를 비트 OR 연산
        const combinedBinary = (arr1[i] | arr2[i]).toString(2);
        
        // 자리에 맞게 앞에 '0' 채우기
        const paddedBinary = combinedBinary.padStart(n, '0');
        
        // 1을 '#', 0을 공백으로 변환
        const change = paddedBinary.replace(/1/g, '#').replace(/0/g, ' ');
        
        result.push(change);
    }
    
    return result;
}