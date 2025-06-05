function solution(book_time) {
    // 문자열을 분 단위 정수로 변환
    const toMinutes = time => {
        const [hh, mm] = time.split(":").map(Number);
        return hh * 60 + mm;
    };
    
    // 예약 시작과 끝을 숫자로 변환하고 정렬
    const bookings = book_time.map(([start, end]) => {
        return [toMinutes(start), toMinutes(end) + 10]; // 퇴실 후 청소시간 10분
    }).sort((a, b) => a[0] - b[0]); // 시작 시간 기준으로 정렬
    
    // 방들의 종료시간 저장
    const rooms = [];
    
    for (const [start, end] of bookings) {
        let available = false;
        
        // 종료된 방 중 가장 먼저 끝나는 방을 재사용할 수 있는지 확인
        for (let i = 0; i < rooms.length; i++) {
            if (rooms[i] <= start) {
                rooms[i] = end; // 이 방을 사용
                available = true;
                break;
            }
        }
        
        // 재사용 가능한 방이 없으면 새 방 추가
        if (!available) {
            rooms.push(end);
        }
    }
    
    return rooms.length;    // 필요한 방의 수
}