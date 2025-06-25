function solution(record) {
    const userMap = {}; // userId -> nickname
    const actions = []; // 메시지 기록을 위한 (action, userId)
    
    for (const line of record) {
        const [cmd, uid, name] = line.split(" ");
        
        if (cmd === "Enter" || cmd === "Change") {
            userMap[uid] = name; // 최종 닉네임 저장
        }
        
        if (cmd === "Enter" || cmd === "Leave") {
            actions.push({ cmd, uid }); // 메시지를 남길 행동만 기록
        }
    }
    
    return actions.map(({ cmd, uid }) => {
        const nickname = userMap[uid];
        if (cmd === "Enter") return `${nickname}님이 들어왔습니다.`;
        if (cmd === "Leave") return `${nickname}님이 나갔습니다.`;
    });
}