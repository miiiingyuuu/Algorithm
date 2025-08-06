function solution(enroll, referral, seller, amount) {
    const profitMap = new Map();
    const parentMap = new Map();
    
    // 추천인 관계 설정
    for (let i = 0; i < enroll.length; i++) {
        profitMap.set(enroll[i], 0);
        parentMap.set(enroll[i], referral[i]);
    }
    
    // 각 판매 실적을 순회하며 이익금 분배
    for (let i = 0; i < seller.length; i++) {
        const currentSeller = seller[i];
        let profit = amount[i] * 100;
        
        let currentPerson = currentSeller;
        
        // 분배할 이익이 1원 이상이고, 추천인이 있는 동안 반복
        while (currentPerson !== "-" && profit > 0) {
            const commission = Math.floor(profit * 0.1);
            
            const myProfit = profit - commission;
            
            // 현재 판매원의 누적 이익금에 방금 계산된 이익을 더하기
            profitMap.set(currentPerson, profitMap.get(currentPerson) + myProfit);
            
            profit = commission
            
            currentPerson = parentMap.get(currentPerson);
        }
    }
    
    // 최초 입력된 enroll 배열 순서에 맞게 최종 이익금 배열을 생성하여 반환함
    const result = enroll.map(name => profitMap.get(name));
    
    return result;
}