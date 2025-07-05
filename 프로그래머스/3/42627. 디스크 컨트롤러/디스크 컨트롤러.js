function solution(jobs) {
    const n = jobs.length;
    if (n === 0) {
        return 0;
    }
    
    // 문제의 세 번째 우선순위 조건인 '작업의 번호가 작은 것'을 처리하기 위한 새로운 배열
    const indexedJobs = jobs.map((job, index) => [...job, index]);
    
    // 1. 요청 시점을 기준으로 오름차순 정렬
    indexedJobs.sort((a, b) => a[0] - b[0]);
    
    const waitingQueue = []; 
    let currentTime = 0;
    let totalTurnaroundTime = 0;    // 모든 작업의 반환 시간 총합
    let jobsCompleted = 0;  // 완료된 작업 수
    let jobIndex = 0;   // 처리할 작업의 인덱스
    
    while (jobsCompleted < n) {
        // 2. currentTime까지 요청된 모든 작업을 대기 큐에 넣기
        while (jobIndex < n && indexedJobs[jobIndex][0] <= currentTime) {
            waitingQueue.push(indexedJobs[jobIndex]);
            jobIndex++;
        }
        
        if (waitingQueue.length > 0) {
            // 3. 대기 큐를 우선순위에 따라 정렬(소요 시간 -> 요청 시각 -> 작업 번호)
            waitingQueue.sort((a, b) => {
                if (a[1] !== b[1]) {
                    return a[1] - b[1];
                }
                if (a[0] !== b[0]) {
                    return a[0] - b[0];
                }
                return a[2] - b[2];
            });
            
            // 4. 우선순위가 가장 높은 작업을 꺼내서 처리
            const currentJob = waitingQueue.shift();
            const [requestTime, duration] = currentJob;
            
            currentTime += duration;
            totalTurnaroundTime += currentTime - requestTime;
            jobsCompleted++;
        } else {
            // 5. 대기 큐가 비어있다면, 다음 작업의 요청 시점으로 시간을 점프
            if (jobIndex < n) {
                currentTime = indexedJobs[jobIndex][0];
            }
        }
    }
    
    // 6. 평균 반환 시간을 계산하여 정수 부분만 반환
    return Math.floor(totalTurnaroundTime / n);
}