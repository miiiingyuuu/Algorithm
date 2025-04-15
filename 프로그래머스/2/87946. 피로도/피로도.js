function solution(k, dungeons) {
    let maxDungeons = 0;
    
    const n = dungeons.length;
    const visited = Array(n).fill(false);
    
    function explore(currentK, count) {
        maxDungeons = Math.max(maxDungeons, count);
        
        for (let i = 0; i < n; i++) {
            if (!visited[i] && currentK >= dungeons[i][0]) {
                visited[i] = true;
                
                explore(currentK - dungeons[i][1], count + 1);
                
                visited[i] = false;
            }
        }
    }
    
    explore(k, 0);
    
    return maxDungeons;
}