
function swap_num(arr) {

    var i = 0;
    var j = arr.length-1;
    var temp = 0;

console.log(arr);

    while( i<= j) {

    for( i=0; i<= arr.length-1; i+=2){
        
       temp= arr[j];
       arr[j]=a[i];
       arr[i]=temp;
       j= j-2;

    }

    }

    console.log(arr);
return;
}
arr[1,2,4,5,a,8,9,0,w];
swap_num(arr);


    var arr = [1,3,9,8,9,0,6,5];
    var i=0;
    var j=arr.length-1;
    var temp=0;
    
    console.log(arr);

    while( i<= j) { // i =0,j=7  {i=2},

    for( i= 0; i<= arr.length-1; i+=2){
        
       temp= arr[j];    //temp=5,ar[7]=1,arr[1]=5
       arr[j]=arr[i];
       arr[i]=temp;
       j= j-2;

    }
    }
    console.log(arr);




    function swap_num() {
        var arr= [1,2,3,46,7,9,0,-2,11];
        var i = 0;
        var j = arr.length-1;
        var temp = 0;
     
    console.log(arr);
    
        while( i<= j) {//reverse array
    
        for( i=0; i<= arr.length-1; i+=2){
            
           temp= arr[j];
           arr[j]=arr[i];
           arr[i]=temp;
           j= j-2;
    
        }
    
        }//reverse array
    
        console.log(arr);

    }
    
    swap_num();


  function swap_num(arr){
    
    var i=0;
    var j=arr.length-1;
    var temp=0;
    
    console.log(arr);

    

    for( i= 0; i<= j; i+=2){
        
       temp= arr[j];   
       arr[j]=arr[i];
       arr[i]=temp;
       j= j-2;

    }
}
    var arr=[1,4,9,3,1,4,0,7,8,5,3,6,0,7,9,0];
    console.log(arr);
    swap_num(arr);
    console.log(arr);