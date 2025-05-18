function solution(numbers) {
    const nums = numbers.map(String);
    
    // 두 숫자를 더해서 큰 순으로 정렬
    nums.sort((a, b) => (b + a) - (a + b));
    
    if (nums[0] === '0') return '0';
    
    return nums.join('');
}