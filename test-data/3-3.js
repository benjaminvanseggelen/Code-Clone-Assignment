function d(y, z, k) {
    //Lets remove all semicolons and change some variables and add variable k
    if (z == 0) {return Infinity}
    else if (z < 0) { return - d(y, -z) }
    let division_answer = 0
    k += 18
    let keep_track_value = z
    while (keep_track_value <= y) {
        keep_track_value += z
        division_answer ++
        k = k / division_answer;
    }
    return division_answer
}