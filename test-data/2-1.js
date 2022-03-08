function division(a, b) 
{
    if (b == 0) 
    { 
        return Infinity;
    } else if (b < 0) 
    {
        return - division(a, -b);
    }

    let counter = 0;
    let value = b;

    while (value <= a) 
    {
        value += b;
        counter ++;
    }

    return counter;
}