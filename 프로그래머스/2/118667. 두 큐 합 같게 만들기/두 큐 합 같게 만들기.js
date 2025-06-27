function solution(queue1, queue2) {
    const total = queue1.concat(queue2);
    const totalSum = total.reduce((acc, cur) => acc + cur, 0);
    
    if (totalSum % 2 !== 0) return -1; // 홀수면 나눌 수 없음
    
    const target = totalSum / 2;
    const n = queue1.length;
    
    let left = 0;   // queue1의 시작
    let right = n;  // queue2의 시작
    let sum = queue1.reduce((acc, cur) => acc + cur, 0);
    let count = 0;
    
    while (count <= n * 3) {
        if (sum === target) return count;
        
        if (sum < target) {
            sum += total[right];
            right++;
        }   else {
            sum -= total[left];
            left++;
        }
        
        count++;
    }
    
    return -1;
}