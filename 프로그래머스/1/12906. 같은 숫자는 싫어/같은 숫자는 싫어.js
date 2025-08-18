function solution(arr) {
    const N = arr.length;
    const answer = [];
    let num = -1;
    
    for (let i = 0; i < N; i++) {
        if (num === arr[i]) {
            continue;
        }   else {
            answer.push(arr[i]);
            num = arr[i];
        }
    }
    
    return answer;
}