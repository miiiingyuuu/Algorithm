function solution(n, words) {
    const useWords = new Set()
    
    useWords.add(words[0])
    
    let lastChar = words[0][words[0].length - 1]
    
    for (let i=1; i < words.length; i++) {
        const currentWord = words[i]
        const currentFirstChar = currentWord[0]
        
        const playerNumber = (i % n) + 1
        const turn = Math.floor(i / n) + 1
        
        if (
            currentWord.length <= 1 ||
            currentFirstChar !== lastChar ||
            useWords.has(currentWord)
        ) {
            return [playerNumber, turn]
        }
        
        useWords.add(currentWord)
        lastChar = currentWord[currentWord.length - 1]
    }
    
    return [0, 0]
}