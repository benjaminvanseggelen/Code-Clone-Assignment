function div(a, b) {
    if (b == 0) { 
        //More comments
        return Infinity;
    } else if (b < 0) {
        //Testing
        return - div(a, -b);
    }

    let i = 0;
    let value = b;

    while (value <= a) {
        value += b;
        i ++;
    }

    return i;
}