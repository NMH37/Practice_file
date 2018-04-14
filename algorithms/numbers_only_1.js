
var arr=["tomatoes",1,3,2,"t",45, "dd"];
console.log(arr);


for (var i = 0; i <= arr.length-1; i++){
       for( var j = arr.length-1; j<=i; j--){
                 if (typeof arr[i] !== "number") {
                     if( typeof arr[j] === "number"){
                             temp = arr[i];
                             arr[i] = arr[j];
                             arr[j]= temp;
                             arr.pop();
                     }
          }           else
        
          
        }
}
  


console.log(arr);