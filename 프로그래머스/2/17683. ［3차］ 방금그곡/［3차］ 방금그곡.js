function solution(m, musicinfos) {
    // '#'이 붙은 음을 다른 문자로 치환해야 함
    // 'C#' -> 'c', 'D#' -> 'd'... 한 글자로 변경
    const replaceSharps = (melody) => {
        return melody
            .replace(/C#/g, 'c')
            .replace(/D#/g, 'd')
            .replace(/F#/g, 'f')
            .replace(/G#/g, 'g')
            .replace(/A#/g, 'a')
            .replace(/B#/g, 'b');
    };
    
    // 1. 기억하는 멜로디의 '#'을 먼저 치환
    const rememberMelody = replaceSharps(m);
    
    // 조건에 맞는 후보 곡들을 저장할 배열
    const candidates = [];
    
    // 2. 각 음악 정보를 순회
    for (let i = 0; i < musicinfos.length; i++) {
        const [startTime, endTime, title, sheetMusic] = musicinfos[i].split(',');
        
        // 재생 시간을 분 단위로 계산
        const startMinutes = Number(startTime.slice(0, 2)) * 60 + Number(startTime.slice(3));
        let endMinutes = Number(endTime.slice(0, 2)) * 60 + Number(endTime.slice(3));
        
        if (endMinutes < startMinutes) {
            endMinutes = 24 * 60; 
        }
        
        const playDuration = endMinutes - startMinutes;
        
        // 해당 곡의 악보도 '#'을 치환
        const processedSheetMusic = replaceSharps(sheetMusic);
        const sheetLength = processedSheetMusic.length;
        
        // 재생 시간만큼의 전체 멜로디를 생성
        const fullMelodyPlayed = processedSheetMusic
            .repeat(Math.ceil(playDuration / sheetLength))
            .substring(0, playDuration);
        
        // 3. 전체 재생된 멜로디에 네오가 기억한 멜로디가 포함되는지 확인
        if (fullMelodyPlayed.includes(rememberMelody)) {
            // 포함된다면 후보 목록에 제목, 재생시간, 입력순서를 추가
            candidates.push({ title, duration: playDuration, index: i });
        }
    }
    
    // 4. 조건에 맞는 최종 곡 결정
    if (candidates.length === 0) {
        return "(None)";
    }
    
    // 후보 곡들을 정렬, 1순위: 재생 시간이 긴 순서(내림차순) / 2순위: 먼저 입력된 순서(오름차순)
    candidates.sort((a, b) => {
        if (a.duration !== b.duration) {
            return b.duration - a.duration;
        }
        return a.index - b.index;
    });
    
    // 정렬 후 가장 앞에 있는 곡의 제목을 반환
    return candidates[0].title;
}