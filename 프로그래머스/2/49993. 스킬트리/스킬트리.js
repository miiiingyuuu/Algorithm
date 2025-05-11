function solution(skill, skill_trees) {
    let count = 0;
    
    for (let tree of skill_trees) {
        let filtered = [...tree].filter(char => skill.includes(char)).join('');
        if (skill.startsWith(filtered)) {
            count++;
        }
    }
    
    return count;
}