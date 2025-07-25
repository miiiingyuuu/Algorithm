function solution(money) {
    const n = money.length;
    
    if (n === 1) {
        return money[0];
    }
    
    const robLinear = (houses) => {
        let prev1 = 0;
        let prev2 = 0;
        
        for (const currentMoney of houses) {
            const temp = prev1;
            prev1 = Math.max(prev1, prev2 + currentMoney);
            prev2 = temp;
        }
        
        return prev1;
    }
    
    // 첫 번째 집을 털고, 마지막 집은 털지 않는 경우
    const maxCase1 = robLinear(money.slice(0, n - 1));
    
    // 첫 번째 집을 털지 않고, 마지막 집은 턴 경우
    const maxCase2 = robLinear(money.slice(1));
    
    return Math.max(maxCase1, maxCase2);
}