function solution(progresses, speeds) {
    const days = progresses.map((progress, index) => {
        return Math.ceil((100 - progress) / speeds[index]);
    });
    
    const result = [];
    let deployDay = days[0];
    let count = 1;
    
    for (let i = 1; i < days.length; i++) {
        if (days[i] <= deployDay) {
            count++;
        } else {
            result.push(count);
            deployDay = days[i]
            count = 1;
        }
    }
    
    result.push(count)
    
    return result
}