function div(a, b, c) {
    if (b == 0) { 
        return Infinity;
    } else if (b < 0) {
        return - div(a, -b);
    }

    c = 0;
    
    let i = 0;
    let x = b;

    while (x <= a) {
        x += b;
        i ++;
    }
    c+=1;
    return i;
}