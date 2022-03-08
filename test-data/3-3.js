function div(a, b) 
{
    if (b == 0) 
    { 
        return Infinity;
    } else if (b < 0) 
    {
        return - div(a, -b);
    }

    let i = 0;
    let x_value = 10;
    x_value = b;

    while (x_value <= a) 
    {
        x_value += b;
        i ++;
    }

    return i;
}