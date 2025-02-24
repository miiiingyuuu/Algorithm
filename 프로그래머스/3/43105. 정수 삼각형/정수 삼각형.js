function solution(triangle) {
    const height = triangle.length
    const dp = Array.from({length: height}, (_, i) =>
                         new Array(i + 1).fill(0)
                         )
    
    dp[0][0] = triangle[0][0]
    
    for (let i = 1; i < height; i++) {
        for (let j = 0; j <= i; j++) {
            const current = triangle[i][j]
            
            if (j === 0) {
                dp[i][j] = dp[i-1][j] + current
            } else if (j === i) {
                dp[i][j] = dp[i-1][j-1] + current
            } else {
                dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + current
            }
        }
    }
    
    return Math.max(...dp[height-1])
}