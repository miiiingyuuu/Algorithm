class MinHeap {
    constructor() {
        this.heap = [];
    }
    
    push(value) {
        this.heap.push(value);
        this._up();
    }
    
    pop() {
        if (this.heap.length === 1) return this.heap.pop();
        const min = this.heap[0];
        this.heap[0] = this.heap.pop();
        this._down();
        return min;
    }
    
    peek() {
        return this.heap[0];
    }
    
    size() {
        return this.heap.length;
    }
    
    _up() {
        let index = this.heap.length - 1;
        const value = this.heap[index];
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            const parent = this.heap[parentIndex];
            if (parent <= value) break;
            this.heap[parentIndex] = value;
            this.heap[index] = parent;
            index = parentIndex;
        }
    }
    
    _down() {
        let index = 0;
        const length = this.heap.length;
        const value = this.heap[0];
        
        while (true) {
            let left = 2 * index + 1;
            let right = 2 * index + 2;
            let smallest = index;
            
            if (left < length && this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }
            if (right < length && this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }
            if (smallest === index) break;
            
            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}

function solution(scoville, K) {
    const heap = new MinHeap();
    for (let s of scoville) heap.push(s);
    
    let count = 0;
    
    while (heap.size() >= 2 && heap.peek() < K) {
        const first = heap.pop();
        const second = heap.pop();
        const mixed = first + second * 2;
        heap.push(mixed);
        count++;
    }
    
    return heap.peek() >= K ? count : -1;
}