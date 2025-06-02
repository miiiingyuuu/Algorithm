function solution(numbers) {
    return numbers.map(x => {
        if (x % 2 === 0) {
            // 짝수: x + 1만 해도 비트 1개만 다름
            return x + 1;
        } else {
            // 홀수: 가장 오른쪽 0을 1로 바꾸고, 그보다 오른쪽의 1을 0으로 바꾸기
            let bin = '0' + x.toString(2);  // 앞에 0 붙여 처리
            let idx = bin.lastIndexOf('0') // 마지막 0 찾기
            let arr = bin.split('');
            arr[idx] = '1';
            arr[idx + 1] = '0';
            return parseInt(arr.join(''), 2);
        }
    })
}