function solution(arr1, arr2) {
    const rows1 = arr1.length;
    const cols1 = arr1[0].length;
    const cols2 = arr2[0].length;
    
    const result = Array(rows1).fill().map(() => Array(cols2).fill(0));
    
    for (let i = 0; i < rows1; i++) {
        for (let j = 0; j < cols2; j++) {
            for (let k = 0; k < cols1; k++) {
                result[i][j] += arr1[i][k] * arr2[k][j];
            }
        }
    }
    
    return result;
}