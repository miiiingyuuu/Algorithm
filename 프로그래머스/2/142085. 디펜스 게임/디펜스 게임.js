class MaxHeap {
    constructor() {
        this.heap = [];
    }

    push(val) {
        this.heap.push(val);
        this._heapifyUp();
    }

    pop() {
        const max = this.heap[0];
        const end = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = end;
            this._heapifyDown();
        }
        return max;
    }

    _heapifyUp() {
        let idx = this.heap.length - 1;
        const element = this.heap[idx];

        while (idx > 0) {
            let parentIdx = Math.floor((idx - 1) / 2);
            let parent = this.heap[parentIdx];

            if (element <= parent) break;

            this.heap[idx] = parent;
            idx = parentIdx;
        }
        this.heap[idx] = element;
    }

    _heapifyDown() {
        let idx = 0;
        const length = this.heap.length;
        const element = this.heap[0];

        while (true) {
            let leftChildIdx = 2 * idx + 1;
            let rightChildIdx = 2 * idx + 2;
            let swap = null;

            if (leftChildIdx < length) {
                if (this.heap[leftChildIdx] > element) {
                    swap = leftChildIdx;
                }
            }

            if (rightChildIdx < length) {
                if (
                    (swap === null && this.heap[rightChildIdx] > element) ||
                    (swap !== null && this.heap[rightChildIdx] > this.heap[leftChildIdx])
                ) {
                    swap = rightChildIdx;
                }
            }

            if (swap === null) break;

            this.heap[idx] = this.heap[swap];
            idx = swap;
        }
        this.heap[idx] = element;
    }
}

function solution(n, k, enemy) {
    let heap = new MaxHeap();
    let soldier = n;
    
    for (let i = 0; i < enemy.length; i++) {
        soldier -= enemy[i];
        heap.push(enemy[i]);
        
        if (soldier < 0) {
            if (k > 0) {
                let maxEnemy = heap.pop();
                soldier += maxEnemy;
                k--;
            } else {
                return i;
            }
        }
    }
    
    return enemy.length;
}