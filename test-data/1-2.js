function div(a, b) {
    if (b == 0) {return Infinity}
    else if (b < 0) {return - div(a, -b)}

    let i = 0;
    let x = b;

    while (x <= a)
    {
        x += b;
        i ++;
    }

    return i;
}