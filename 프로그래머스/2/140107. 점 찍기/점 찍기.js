function solution(k, d) {
    let answer = 0;
    
    // x좌표를 k씩 증가시키며 d까지 반복
    for (let x = 0; x <= d; x += k) {
        // 현재 x좌표에서 원점과의 거리가 d를 넘지 않는 최대 y값 계산
        const yMax = Math.sqrt(d * d - x * x);
        
        // y좌표 또한 k의 배수여야 함 -> yMax를 k로 나눈 몫이 가능한 b의 최대값
        answer += Math.floor(yMax / k) + 1;
    }
    
    return answer;
}