function solution(picks, minerals) {
    let answer = 0;
    const [diaPick, ironPick, stonePick] = picks;
    const totalPicks = diaPick + ironPick + stonePick;
    
    // 1. 캘 수 있는 만큼만 광물 배열 자르기
    const minableMinerals = minerals.slice(0, totalPicks * 5);
    
    // 피로도 표: fatigue[곡갱이종류][광물종류]
    const fatigueTable = {
        diamond: { diamond: 1, iron: 1, stone: 1 },
        iron: { diamond: 5, iron: 1, stone: 1 },
        stone: { diamond: 25, iron: 5, stone: 1 },
    };
    
    // 2. 광물을 5개씩 묶어서 각 묶음에 대한 피로도를 각각의 곡갱이로 진행했을 때 피로도 계산
    const checkFatigue = [];
    for (let i = 0; i < minableMinerals.length; i += 5) {
        const chunk = minableMinerals.slice(i, i+5);
        const fatigue = { diamond: 0, iron: 0, stone: 0 };
        
        chunk.forEach(mineral => {
            fatigue.diamond += fatigueTable.diamond[mineral];
            fatigue.iron += fatigueTable.iron[mineral];
            fatigue.stone += fatigueTable.stone[mineral];
        });
        
        checkFatigue.push(fatigue);
    }
    
    // 3. 돌 곡갱이를 기준으로, 피로도가 높은 순으로 묶음 정렬(좋은 곡갱이로 처리할 수록 좋다는 뜻)
    checkFatigue.sort((a, b) => b.stone - a.stone);
    
    // 4. 정렬된 묶음에 대해 좋은 곡갱이부터 사용하여 피로도를 최소로 누적
    let currentPicks = [...picks];
    checkFatigue.forEach(fatigue => {
        if (currentPicks[0] > 0) {
            answer += fatigue.diamond;
            currentPicks[0]--;
        }   else if (currentPicks[1] > 0) {
            answer += fatigue.iron;
            currentPicks[1]--;
        }   else if (currentPicks[2] > 0) {
            answer += fatigue.stone;
            currentPicks[2]--;
        }
    });
    
    return answer;
}