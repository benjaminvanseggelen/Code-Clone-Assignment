function a(b, c){if(c == 0){return Infinity;}else if(c < 0){return -a(b,-c);}let d=0;let x=c;while(x<=b){x+=c;d++;}return d;}
