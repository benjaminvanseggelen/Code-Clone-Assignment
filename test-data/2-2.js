function d(y, z) {
    if (z == 0) { return Infinity; }
    else if (z < 0) { return - d(y, -z); }
    let b = 0;
    let a = z;
    while (a <= y) { a += z; b ++; }
    return b;
}