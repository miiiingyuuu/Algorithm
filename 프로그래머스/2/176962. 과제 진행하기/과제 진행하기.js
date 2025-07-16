function solution(plans) {
    // 시간을 분으로 변환 후 시작 시간 기준으로 정렬
    const processedPlans = plans.map(plan => {
        const [name, start, playtime] = plan;
        const [hour, minute] = start.split(":").map(Number);
        const startInMinutes = hour * 60 + minute;
        return {
            name,
            start: startInMinutes,
            playtime: Number(playtime)
        };
    }).sort((a, b) => a.start - b.start);
    
    const finishedTasks = [];   // 완료된 과제를 저장할 배열
    const pausedTasks = [];     // 멈춘 과제를 저장할 배열
    
    let currentTime = 0;
    
    for (let i = 0; i < processedPlans.length; i++) {
        const currentTask = processedPlans[i];
        
        // 다음 과제가 있는 경우와 없는 경우를 구분
        const nextTask = processedPlans[i + 1];
        let availableTime;
        
        if (nextTask) {
            availableTime = nextTask.start - currentTask.start;
        }   else {
            // 마지막 과제는 시간이 무한하다고 가정
            availableTime = Infinity;
        }
        
        // 현재 과제를 끝낼 수 있는지 확인
        if (availableTime >= currentTask.playtime) {
            // 현재 과제를 시간 내에 끝낼 수 있음
            finishedTasks.push(currentTask.name);
            let remainingTime = availableTime - currentTask.playtime;
            
            // 남는 시간 동안 멈췄던 과제 처리
            while (remainingTime > 0 && pausedTasks.length > 0) {
                const paused = pausedTasks.pop();   // 가장 최근에 멈춘 과제
                
                if (remainingTime >= paused.playtime) {
                    finishedTasks.push(paused.name);
                    remainingTime -= paused.playtime;
                }   else {
                    paused.playtime -= remainingTime;
                    pausedTasks.push(paused);
                    remainingTime = 0;
                }
            }
        }   else {
            // 현재 과제를 끝내기 전에 다음 과제를 시작해야 함
            currentTask.playtime -= availableTime;
            pausedTasks.push(currentTask);
        }
    }
    
    // 모든 계획을 순회한 후, 스택에 남아 있는 과제들을 마무리
    while (pausedTasks.length > 0) {
        finishedTasks.push(pausedTasks.pop().name);
    }
    
    return finishedTasks;
}