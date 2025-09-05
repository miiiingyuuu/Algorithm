function solution(name, yearning, photo) {
    const yearningMap = name.reduce((acc, currentName, index) => {
        acc[currentName] = yearning[index];
        return acc;
    }, {});
    
    const result = photo.map(singlePhoto =>
        singlePhoto.reduce((sum, person) => {
            return sum + (yearningMap[person] || 0)
        }, 0)
    );
    
    return result;
}