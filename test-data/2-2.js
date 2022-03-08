function div(value1, b) {
    if (b == 0) { return Infinity; } else if (b < 0) { return - div(value1, -b); }

    let i = 0;
    let x = b;

    while (x <= value1) {
        x += b;
        i ++;
    }

    return i;
}