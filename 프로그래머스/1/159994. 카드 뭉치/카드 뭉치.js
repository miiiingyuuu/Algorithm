function solution(cards1, cards2, goal) {
    let index1 = 0;
    let index2 = 0;
    
    for (let i = 0; i < goal.length; i++) {
        const currentWord = goal[i];
        
        if (index1 < cards1.length && cards1[index1] === currentWord) {
            index1++;
        }   else if (index2 < cards2.length && cards2[index2] === currentWord) {
            index2++;
        }   else {
            return "No";
        }
    }
    
    return "Yes";
}