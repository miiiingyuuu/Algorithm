function solution(orders, course) {
    const answer = [];
    
    // 1. course 배열의 각 원소에 대해 반복
    for (const courseSize of course) {
        const combinations = new Map();
        let maxCount = 0;
        
        // 2. 각 손님의 주문(order)에 대해 반복
        for (const order of orders) {
            // 주문한 메뉴 수가 코스 요리 길이보다 짧으면 조합을 만들 수 없음
            if (order.length < courseSize) continue;
            
            // 3. 조합을 만들기 위한 재귀 함수
            const sortedOrder = order.split('').sort();
            
            const getCombinations = (startIndex, currentCombo) => {
                // 현재 조합의 길이가 원하는 코스 길이와 같아지면 조합의 카운트 + 1
                if (currentCombo.length === courseSize) {
                    const count = (combinations.get(currentCombo) || 0) + 1;
                    combinations.set(currentCombo, count);
                    
                    // 최대 주문 횟수를 갱신
                    if (count > maxCount) {
                        maxCount = count;
                    }
                    return;
                }
                
                for (let i = startIndex; i < sortedOrder.length; i++) {
                    getCombinations(i + 1, currentCombo + sortedOrder[i]);
                }
            };
            
            getCombinations(0, "");
        }
        
        // 4. 최대 주문 횟수가 2 이상인 경우에만 결과에 추가
        if (maxCount >= 2) {
            for (const [combo, count] of combinations.entries()) {
                if (count === maxCount) {
                    answer.push(combo);
                }
            }
        }
    }
    
    // 5. 최종 결과를 사전 순으로 정렬
    return answer.sort();
}