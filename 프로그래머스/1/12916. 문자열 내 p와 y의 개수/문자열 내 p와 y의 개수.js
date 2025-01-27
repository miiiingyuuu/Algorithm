function solution(s){
    const text = s.toLowerCase();
    const pCount = (text.match(/p/g) || []).length;
    const yCount = (text.match(/y/g) || []).length;
    return pCount === yCount;    
}