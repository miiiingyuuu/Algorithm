function solution(scores) {
    const wanho = scores[0];
    const wanhoSum = wanho[0] + wanho[1];
    
    // 근무 태도 점수 내림차순, 동료 평가 점수 오름차순으로 정렬
    scores.sort((a, b) => {
        if (a[0] !== b[0]) {
            return b[0] - a[0];
        }
        
        return a[1] - b[1];
    });
    
    let maxPeerScore = 0;
    const eligibleSums = [];
    
    // 배열을 순회하며 인센티브 대상자를 찾고, 완호의 자격 확인
    for (const score of scores) {
        // 현재까지 나온 동료 평가 점수 최댓값보다 현재 동료 평가 점수가 낮다면, 이 직원은 인센티브 x
        if (score[1] < maxPeerScore) {
            // 대상이 완호면 x
            if (score === wanho) {
                return -1;
            }
        } else {
            // 인센티브 대상자인 경우
            maxPeerScore = Math.max(maxPeerScore, score[1]);
            eligibleSums.push(score[0] + score[1]);
        }
    }
    
    // 인센티브 대상자들의 점수 합계 목록에서 완호의 석차 계산
    let rank = 1;
    for (const sum of eligibleSums) {
        if (sum > wanhoSum) {
            rank++;
        }
    }
    
    return rank;
}