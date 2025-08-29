function solution(food) {
    // 0을 기준으로 오른쪽, 왼쪽 나눠 음식 순서 알아보기
    const left = food.slice(1).map((count, i) => {
        const foodNumber = i + 1;
        const numToTake = Math.floor(count / 2);
        return String(foodNumber).repeat(numToTake);
    })
    .join('');
    
    const right = left.split('').reverse().join('');
    
    return left + '0' + right;
}