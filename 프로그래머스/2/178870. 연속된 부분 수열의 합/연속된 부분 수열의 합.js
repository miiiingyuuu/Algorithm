function solution(sequence, k) {
    let left = 0, right = 0;
    let sum = sequence[0];
    let minLen = Infinity;
    let answer = [0, 0];
    
    while (right < sequence.length) {
        if (sum === k) {
            // 현재 구간 길이
            const len = right - left + 1;
            // 더 짧거나, 같은 길이고 더 앞쪽이라면 갱신
            if (len < minLen) {
                minLen = len;
                answer = [left, right];
            }
            // sum이 k면 오른쪽을 확장해도 sum이 커지므로 왼쪽을 줄이기
            sum -= sequence[left++];
        } else if (sum < k) {
            // k보다 작으면 오른쪽 확장
            right++;
            if (right < sequence.length) {
                sum += sequence[right];
            }
        } else {
            // k보다 크면 왼쪽 축소
            sum -= sequence[left++];
        }
    }
    
    return answer;
}