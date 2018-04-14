
function printRange(low ,high,skip=1){

    var low;
    var high;
    var skip;
 
    
    if (!high)
    {  
        if ( low<0){
        high = 0;
        } 
        else 
        high = low;
        low = 0;
        
    }
    
for ( i= low; i < high; i= i + skip ){


 console.log( i);

}
}
printRange(-122);