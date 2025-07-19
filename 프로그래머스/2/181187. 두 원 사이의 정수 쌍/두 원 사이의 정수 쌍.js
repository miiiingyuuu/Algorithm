function solution(r1, r2) {
    let answer = 0;

    // 1사분면(x > 0, y > 0) 위의 점 개수 계산
    for (let x = 1; x <= r2; x++) {
        // 1. 바깥 원(r2)을 기준으로 최대 y값 계산
        const maxY = Math.floor(Math.sqrt(r2 * r2 - x * x));

        // 2. 안쪽 원(r1)을 기준으로 최소 y값 계산
        // x가 r1보다 크면, 안쪽 원의 영향이 없으므로 최소 y는 1부터 시작 (즉, 제외할 점이 없음)
        let minYCount = 0;
        if (x < r1) {
            minYCount = Math.floor(Math.sqrt(r1 * r1 - x * x));
            // 만약 sqrt(r1*r1 - x*x)가 정수이면, 해당 점 (x, minYCount)는 경계선 위의 점이다.
            // 경계선 위의 점은 포함해야 하므로, 제외할 점의 개수에서 하나를 빼준다.
            if (Math.sqrt(r1 * r1 - x * x) % 1 === 0) {
                minYCount--;
            }
        }
        
        // 해당 x 좌표에서 두 원 사이의 정수 점 개수를 더한다.
        // (maxY + 1)이 아니라 maxY인 이유는 y=0인 점은 축 위의 점으로 따로 계산하기 때문.
        answer += (maxY - minYCount);
    }

    // 2. 4개 사분면에 대해 동일하므로 4를 곱하고, 축 위의 점 개수를 더한다.
    // 축 위의 점: (r2 - r1 + 1)개가 4개의 축 방향에 존재
    return answer * 4 + (r2 - r1 + 1) * 4;
}