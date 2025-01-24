function solution(N) {
    return String(N)
        .split('')
        .reduce((acc, cur) => acc + Number(cur), 0)
}