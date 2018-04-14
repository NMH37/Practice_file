



function add_odd(low,high){

var num;
var sum =0;
var high;
 low;


for( num=low;  num<=high;  num++){

   if (num % 2 !== 0){
   sum = sum + num;
   }

}
console.log(sum);
}

add_odd(-30000,300000);