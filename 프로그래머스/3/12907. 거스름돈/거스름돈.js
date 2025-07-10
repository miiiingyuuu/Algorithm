function solution(n, money) {
    // dp[i]: i원을 만들 수 있는 방법의 수
    const dp = new Array(n + 1).fill(0);
    const MOD = 1000000007;
    
    dp[0] = 1;  // 0원을 만드는 방법 초기값 입력
    
    for (const coin of money) {
        for (let j = coin; j <= n; j++) {
            // j원을 만드는 방법의 수에 (j-coin)을 만드는 방법의 수를 더함
            dp[j] = (dp[j] + dp[j - coin]) % MOD;
        }
    }
    
    return dp[n];
}