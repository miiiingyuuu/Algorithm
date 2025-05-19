function solution(genres, plays) {
    const genreMap = new Map(); // 장르별 총 재생 수
    const songMap = new Map(); // 장르별 노래 리스트
    
    // 장르별 총 재생 수와 노래 정보 저장
    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i];
        
        // 총 재생 수 저장
        genreMap.set(genre, (genreMap.get(genre) || 0) + play);
        
        // 노래 목록 저장
        if (!songMap.has(genre)) songMap.set(genre, []);
        songMap.get(genre).push([i, play])  // [고유번호, 재생수]
    }
        
        // 장르를 총 재생 수 기준으로 정렬
        const sortedGenres = [...genreMap.entries()].sort((a, b) => b[1] - a[1]).map(entry => entry[0]);
        
        const result = [];
        
        // 각 장르에서 재생 수가 많은 노래 최대 2개 선택
        for (const genre of sortedGenres) {
            const songs = songMap.get(genre);
            
            // 재생 수는 내림차순, 같다면 고유번호 오름차순 순으로 return
            songs.sort((a, b) => {
                if (b[1] !== a[1]) return b[1] - a[1];  // 재생 수 기준
                return a[0] - b[0]; // 고유 번호 기준
            });
            
            // 최대 2개까지 수록
            result.push(songs[0][0]);
            if (songs.length > 1) result.push(songs[1][0]);
        }
    
    return result;
}