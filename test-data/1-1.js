function div(a, b) {
    // Computes the result of a / b
    if (b == 0) { 
        // We will naturally want to return 0 here
        return Infinity;
    } else if (b < 0) {
        // Simply take the negative of the positive b result
        return - div(a, -b);
    }

    let i = 0;
    let x = b;

    while (x <= a) {
        // Due to the checks at the top of the function, this is safe to do without guard
        x += b;
        i ++;
    }

    return i;
}