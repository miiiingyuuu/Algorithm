function solution(gems) {
    // 1. 전체 보석의 종류 수를 구하기(중복 제거)
    const totalGemTypes = new Set(gems).size;

    // 2. 슬라이딩 윈도우와 정답을 위한 변수 초기화
    let answer = [1, gems.length];
    let start = 0;
    const gemMap = new Map();

    // 3. end 포인터를 이동시키며 윈도우를 확장
    for (let end = 0; end < gems.length; end++) {
        // 현재 end 위치의 보석을 Map에 추가 (없으면 1, 있으면 +1)
        gemMap.set(gems[end], (gemMap.get(gems[end]) || 0) + 1);

        // 4. 윈도우가 모든 종류의 보석을 포함하는 경우, start를 이동시켜 윈도우를 축소
        while (gemMap.size === totalGemTypes) {
            const currentLength = end - start + 1;
            const bestLength = answer[1] - answer[0] + 1;

            // 현재 구간이 기존의 가장 짧은 구간보다 짧으면 정답 갱신
            if (currentLength < bestLength) {
                answer = [start + 1, end + 1];
            }

            // start 위치의 보석을 Map에서 개수 줄이기
            const startGem = gems[start];
            gemMap.set(startGem, gemMap.get(startGem) - 1);

            // 만약 해당 보석의 개수가 0이 되면 Map에서 완전히 제거
            // -> 윈도우가 더 이상 모든 보석을 포함하지 않게 됨
            if (gemMap.get(startGem) === 0) {
                gemMap.delete(startGem);
            }

            start++;
        }
    }

    return answer;
}