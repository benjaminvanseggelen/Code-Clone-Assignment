function d(y, z)
{
    //We also love a single line for every bracket!
    if (z == 0)
    {
        return Infinity;
        //After the return we want to do something else.
        let c = 1;
        c+=10;
    }
    else if (z < 0)
    {
        return - d(y, -z);
    }
    let b = 0;
    let a = z;
    while (a <= y)
    {
        a += z;
        b ++;
    }
    return b;
}