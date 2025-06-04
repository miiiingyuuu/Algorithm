function solution(weights) {
    const counter = new Map();
    let answer = 0;
    
    // 빈도수 카운팅
    for (let w of weights) {
        counter.set(w, (counter.get(w) || 0) + 1);
    }
    
    // 가능한 비율 리스트
    const ratios = [1, 3 / 2, 2, 4 / 3];
    
    for (let [weight, count] of counter) {
        for (let ratio of ratios) {
            const target = weight * ratio;
            if (!Number.isInteger(target)) continue;
            
            if (counter.has(target)) {
                // 같은 무게는 조합 수 공식 nC2 = n*(n-1)//2
                if (weight === target) {
                    answer += (count * (count - 1)) / 2;
                } else if (weight < target) {
                    answer += count * counter.get(target);
                }
            }
        }
    }
    
    return answer;
}