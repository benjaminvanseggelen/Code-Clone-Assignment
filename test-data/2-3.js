function division(a1, a2)
{
    if (a2 == 0)
    {
        return Infinity;
    } else if (a2 < 0)
    {
        return - division(a1, -a2);
    }

    //We define the variables that we need for calculating the division
    let count = 0;
    let c = a2;

    while (c <= a1)
    {
        c += a2;
        count ++;
    }

    return count;
}