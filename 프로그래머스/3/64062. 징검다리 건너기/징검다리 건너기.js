function solution(stones, k) {
    // 그냥 한명씩 건너가면서 돌 내구도를 깎아내리면, 효율성이 안좋을 것. 이진탐색으로 풀기
    let left = 1;
    let right = 200000000;
    let answer = 0;
    
    const canCross = (friendsCount) => {
        let skipCount = 0;  // 연속으로 밟을 수 없는 디딤돌의 수

        for (const stone of stones) {
                if (stone < friendsCount) {
                skipCount++;
            }   else {
                // 밟을 수 있는 돌을 만나면 연속 카운트 초기화
                skipCount = 0;
            }

            // 연속으로 밟을 수 없는 돌의 개수가 k개 이상이면 더 이상 진행 불가
            if (skipCount >= k) {
                return false;
            }
        }
    
        return true;
    };
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        if (canCross(mid)) {
            answer = mid;
            left = mid + 1;
        }   else {
            right = mid - 1;
        }
    }
    
    return answer;
}