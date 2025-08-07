function solution(n, t, m, timetable) {
    // HH:MM을 분으로 바꾸기
    const timeToMin = (time) => {
        const [hour, min] = time.split(':').map(Number);
        
        return hour * 60 + min;
    }
    
    // 분을 HH:MM으로 바꾸기
    const minToTime = (min) => {
        const hour = Math.floor(min / 60);
        const minute = min % 60;
        
        // padStart: 내가 원하는 칸 만큼 빈자리는 '0' 채워줌
        return `${String(hour).padStart(2, '0')}:${String(minute).padStart(2, '0')}`;
    }
    
    // 도착 시간 분으로 변환 후 오름차순 정렬
    const crewTimes = timetable.map(timeToMin).sort((a, b) => a - b);
    
    let shuttleTime = timeToMin("09:00");
    let answer = 0;
    let crewIndex = 0;
    
    for (let i = 0; i < n; i++) {
        let onboardCount = 0;
        
        // 현재 셔틀에 탑승할 수 있는 크루들을 찾기
        while (onboardCount < m && crewIndex < crewTimes.length && crewTimes[crewIndex] <= shuttleTime) {
            onboardCount++;
            crewIndex++;
        }
        
        // 마지막 셔틀일 경우, 콘이 도착할 시간을 계산
        if (i === n-1) {
            // 셔틀에 남는 자리가 있으면 마지막 셔틀 시간에 맞춰 오면 됨
            if (onboardCount < m) {
                answer = shuttleTime;
            }
            
            // 셔틀에 남는 자리가 없다면 마지막으로 탑승한 사람보다 1분 일찍 와야 함
            else {
                answer = crewTimes[crewIndex - 1] - 1;
            }
        }
        
        // 다음 셔틀의 도착 시간 계산
        shuttleTime += t;
    }
    
    return minToTime(answer);
}