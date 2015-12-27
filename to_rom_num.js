function convert(num) {
 var rn = {
   0:"",
   1:"I",
   2:"II",
   3:"III",
   4:"IV",
   5:"V",
   6:"VI",
   7:"VII",
   8:"VIII",
   9:"IX",
   10:"X",
   20:"XX",
   30:"XXX",
   40:"XL",
   50:"L",
   60:"LX",
   70:"LXX",
   80:"LXXX",
   90:"XC",
   100:"C",
   200:"CC",
   300:"CCC",
   400:"CD",
   500:"D",
   600:"DC",
   700:"DCC",
   800:"DCCC",
   900:"CM",
   1000:"M",
   2000:"MM",
   3000:"MMM"
 };
  temp = [];
  for(var i = num.toString().length; i >= 0; i--){
    n = parseInt(num.toString()[i]);
    if(n==0){
      temp.push(0);
    }
    if(n){
      temp.push(n);
    }
  }
  //console.log(temp);
  for(var j = temp.length-1; j> 0; j--){
    temp[j] *= Math.pow(10,j);
  }
  return(temp
              .reverse()
              .map(function(y){
    return rn[y];
  })
              .reduce(function(tol,x){
    return tol+x;
  }));
}
