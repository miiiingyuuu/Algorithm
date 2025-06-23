function solution(fees, records) {
    const [basicTime, basicFee, unitTime, unitFee] = fees;
    const recordMap = new Map();
    const result = new Map();
    
    for (const record of records) {
        const [time, carNumber, status] = record.split(' ');
        const [hour, minute] = time.split(':').map(Number);
        const totalMinutes = hour * 60 + minute;
        
        if (!recordMap.has(carNumber)) {
            recordMap.set(carNumber, []);
        }
        recordMap.get(carNumber).push({ time: totalMinutes, status });
    }
    
    for (const [carNumber, times] of recordMap) {
        let totalParkingTime = 0;
        let lastInTime = null;
        
        for (const { time, status } of times) {
            if (status === 'IN') {
                lastInTime = time;
            }   else {
                totalParkingTime += time - lastInTime;
                lastInTime = null;
            }
        }
        
        if (lastInTime !== null) {
            totalParkingTime += (23 * 60 + 59) - lastInTime;
        }
        
        let parkingFee = basicFee;
        if (totalParkingTime > basicTime) {
            parkingFee += Math.ceil((totalParkingTime - basicTime) / unitTime) * unitFee;
        }
        
        result.set(carNumber, parkingFee);
    }

    const sortedResult = [...result.entries()].sort((a, b) => a[0].localeCompare(b[0]));
    
    return sortedResult.map(([, fee]) => fee)
}