function solution(sticker) {
    // 첫 번째 스티커를 사용하는 경우와 사용하지 않는 경우로 나눠 계산
    const n = sticker.length;   
    const dp1 = Array(n).fill(0);
    const dp2 = Array(n).fill(0);
    
    dp1[0] = sticker[0];
    dp1[1] = sticker[0];
    dp2[1] = sticker[1];
    
    for (let i = 2; i < n; i++) {
        if (i !== n - 1) {
            dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + sticker[i]);
        } else {
            dp1[i] = dp1[i - 1];
        }
        
        dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i]);
    }
    
    return Math.max(dp1[n - 1], dp2[n - 1]);
}