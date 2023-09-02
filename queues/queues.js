class MyStack {
    constructor() {
        this.q = [];
    }

    push(x) {
        this.q.push(x);
    }

    pop() {
        for (let i = 0; i < this.q.length; i++) {
            this.push(this.q.shift());
        }
        return this.q.shift();
    }

    top() {
        return this.q[this.q.length - 1];
    }

    empty() {
        return this.q.length === 0;
    }
}