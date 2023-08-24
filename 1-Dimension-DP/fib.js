function climbStairs(n) {
    if (n <= 2){ return 1 };
    let one = 1, two = 1;

    for (let i = 0; i < n - 1; i++) {
        const temp = one;
        one = one + two;
        two = temp;
    }
    return one;
}

console.log(climbStairs(5));