function solution(users, emoticons) {
    const discounts = [10, 20, 30, 40];
    let maxJoin = 0;
    let maxSales = 0;
    
    function dfs(depth, discountList) {
        if (depth === emoticons.length) {
            let joinCount = 0;
            let totalSales = 0;
            
            for (let [minDiscount, minPrice] of users) {
                let userSpending = 0;
                
                // 사용자의 기준에 맞게 이모티콘 구매 계산
                for (let i = 0; i < emoticons.length; i++) {
                    if (discountList[i] >= minDiscount) {
                        const discountedPrice = emoticons[i] * (100 - discountList[i]) / 100;
                        userSpending += discountedPrice;
                    }
                }
                
                if (userSpending >= minPrice) {
                    // 구매 취소하고 플러스 서비스 가입
                    joinCount += 1;
                }   else {
                    totalSales += userSpending;
                }
            }
            
            // 목표 1 우선, 목표 2 후순위
            if (joinCount > maxJoin || (joinCount === maxJoin && totalSales > maxSales)) {
                maxJoin = joinCount;
                maxSales = totalSales;
            }
            
            return;
        }
        
        for (let discount of discounts) {
            discountList.push(discount);
            dfs(depth + 1, discountList);
            discountList.pop();
        }
    }
    
    dfs(0, []);
    return [maxJoin, Math.floor(maxSales)];
}