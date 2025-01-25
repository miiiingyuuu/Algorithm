function solution(x, n) {
    // n길이의 배열 생성 후, 요소를 x로 채우는데 요소를 순회하며 n의 수만큼 새로운 값을 반환
    return Array(n).fill(x).map((v, i) => v * (i + 1))
}