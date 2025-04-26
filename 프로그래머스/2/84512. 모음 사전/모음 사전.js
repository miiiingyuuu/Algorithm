function solution(word) {
    const vowels = ['A', 'E', 'I', 'O', 'U'];
    const weight = [781, 156, 31, 6, 1];
    let answer = 0;
    
    for (let i = 0; i < word.length; i++) {
        const idx = vowels.indexOf(word[i]);
        answer += idx * weight[i] + 1;
    }
    
    return answer;
}