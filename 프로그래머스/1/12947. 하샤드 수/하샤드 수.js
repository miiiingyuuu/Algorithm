function solution(x) {
    const digits = String(x).split('');
    const sum = digits.reduce((acc, curr) => acc + Number(curr), 0);
    return x % sum === 0;
}