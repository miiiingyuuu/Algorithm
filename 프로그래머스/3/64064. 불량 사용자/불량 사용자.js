function solution(user_id, banned_id) {
    // 1. banned_id 패턴을 정규식으로 변환
    // '*'은 모든 문자(.)와 일치하도록 하고, 문자열 전체가 일치해야 하므로 ^와 $를 추가
    const bannedRegex = banned_id.map(banned => 
        new RegExp(`^${banned.replace(/\*/g, '.')}$`)                               
    );
    
    const resultSet = new Set(); // 최종 조합들을 저장할 Set (중복 제거용)
    
    function dfs(bannedIndex, currentCombination) {
        // 2. 기저 조건: 모든 banned_id에 대해 매칭을 완료한 경우
        if (bannedIndex === banned_id.length) {
            const sortedCombination = Array.from(currentCombination).sort().join(',');
            resultSet.add(sortedCombination);
            return;
        }
        
        const currentRegex = bannedRegex[bannedIndex];
        
        // 3. 재귀: user_id 목록을 순회하며 매칭 시도
        for (const user of user_id) {
            // 이미 조합에 포함된 user_id는 건너뛰기
            if (currentCombination.has(user)) {
                continue;
            }
            
            // 정규식에 매칭되는 user_id를 찾으면 조합에 추가하고 다음 banned_id 인덱스 재귀 호출
            if (currentRegex.test(user)) {
                currentCombination.add(user);
                dfs(bannedIndex + 1, currentCombination);
                // 탐색이 끝난 후, 다른 경우의 수를 위해 조합에서 제거
                currentCombination.delete(user);
            }
        }
    }
    
    dfs(0, new Set());
    
    return resultSet.size;
}