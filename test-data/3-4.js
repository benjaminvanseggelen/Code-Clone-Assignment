//we calculate the division by removing all characters that we don't need and change some statements from negations to -1
function d(a,b){if(b == 0){return Infinity;}else if(b < 0){return-1*d(a,-1*b);}let i=0;let x=b;while(x <= a){x+=b;i+=1;}return i;}