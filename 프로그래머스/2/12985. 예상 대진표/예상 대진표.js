function solution(n,a,b)
{
    let round = 1
    
    while (true) {
        if (Math.ceil(a / 2) === Math.ceil(b / 2)) {
            return round
        }
        
        a = Math.ceil(a / 2)
        b = Math.ceil(b / 2)
        
        round++
    }
}