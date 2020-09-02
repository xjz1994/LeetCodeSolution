class Stack {
    constructor() {
        this.items = [];
        this.count = 0;
    }

    empty() {
        return this.count === 0;
    }

    push(item) {
        this.items.push(item);
        this.count = this.count + 1;
    }

    pop() {
        if (this.count > 0) {
            this.count = this.count - 1;
        }

        return this.items.pop();
    }

    top() {
        return this.items.slice(-1)[0];
    }
}

/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function (prices) {
    let res = new Array(prices.length).fill(0);

    let stack = new Stack();
    prices.push(0);
    for (let i = 0; i < prices.length; i++) {
        while (!stack.empty() && prices[i] <= prices[stack.top()]) {
            res[stack.top()] = prices[stack.top()] - prices[i]; //单调栈
            stack.pop();
        }
        stack.push(i);
    }
    return res;
};

let prices = [8, 4, 6, 2, 3];
let res = finalPrices(prices);
console.log(res);