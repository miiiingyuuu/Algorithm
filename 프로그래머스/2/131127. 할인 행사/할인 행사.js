function solution(want, number, discount) {
    let answer = 0;
    const totalDays = discount.length;
    const membershipDays = 10;
    
    const wantMap = new Map();
    for (let i = 0; i < want.length; i++) {
        wantMap.set(want[i], number[i])
    }
    
    for (let startDay = 0; startDay <= totalDays - membershipDays; startDay++) {
        const currentDiscounts = new Map();
        
        for (let day = 0; day < membershipDays; day++) {
            const product = discount[startDay + day];
            currentDiscounts.set(product, (currentDiscounts.get(product) || 0) + 1);
            
        }
        
        let allProductsAvailable = true;
        for (const [product, quantity] of wantMap) {
            if ((currentDiscounts.get(product) || 0) < quantity) {
                allProductsAvailable = false;
                break;
            }
        }
        
        if (allProductsAvailable) {
            answer++;
        }
    }
    
    return answer;
}