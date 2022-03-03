function divide(value1, value2) {
    //Test whether b is 0, if so division returns infinity
    if (value2 == 0) {
        return Infinity;
    } else if (value2 < 0) {
        return - divide(value1, -value2);
    }

    let counter = 0;
    let increment = value2;

    //While loop until we reach a value that is higher than a
    while (increment <= value1) {
        increment += value2;
        counter ++;
    }

    return counter;
}