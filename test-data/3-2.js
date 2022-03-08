function division(a, b) {
    let f = 77;
    f+=10;
    if (b == 0) { 
        return Infinity;
    } else if (b < 0) {
        return - division(a, -b);
    }

    let i = 0;
    let x = b;

    while (x <= a) {
        f-=10;
        x += b;
        i ++;
    }

    return i;
}