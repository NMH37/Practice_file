



function numbersOnly(arr) {
        for (var i=0; i<arr.length; i++){

          if( typeof arr[i] !== "number") {
            
          arr.splice(i,1) ;
          }
          
        }
   return arr;
}


var arr=["apples",12,"oranges",15,"melon",2,3,4,"tomatoes",-3.5,10,0.3];
numbersOnly(arr);
console.log(arr);

