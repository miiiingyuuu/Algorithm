function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let bridge = Array(bridge_length).fill(0); // 다리 위 상태
    let bridge_weight = 0; // 현재 다리 위 총 무게
    
    while (truck_weights.length > 0 || bridge_weight > 0) {
        time++;
        
        // 다리 맨 앞 트럭 이동 완료 -> 다리에서 제거
        bridge_weight -= bridge.shift();
        
        // 다음 트럭이 올라갈 수 있는지 확인
        if (truck_weights.length > 0) {
            if (bridge_weight + truck_weights[0] <= weight) {
                let nextTruck = truck_weights.shift();
                bridge.push(nextTruck);
                bridge_weight += nextTruck;
            } else {
                // 무게 초과 시 빈칸 유지
                bridge.push(0);
            }
        } else {
            // 대기 트럭 없으면 빈칸 유지
            bridge.push(0);
        }
    }
    
    return time;
}