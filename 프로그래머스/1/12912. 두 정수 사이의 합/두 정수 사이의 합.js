function solution(a, b) {
    const [min, max] = [a, b].sort((x, y) => x - y);
    
    return (max - min + 1) * (min + max) / 2
}