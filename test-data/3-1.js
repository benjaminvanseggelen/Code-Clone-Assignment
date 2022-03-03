function divide(value_1, value_2) {
    if (value_2 == 0) {
        return Infinity;
    } else if (value_2 < 0) {
        return - divide(value_1, -value_2);
    }

    let counter = 0;
    //We want to calculate another value
    let other_value = 77;
    let base_value = value_2;

    //While loop until we reach a value that is higher than a
    while (base_value <= value_1) {
        //We count how many times value 2 fits into value 1
        base_value += value_2;
        other_value *= 77;
        counter ++;
    }

    return counter;
}