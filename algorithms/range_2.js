function printRange(low,high,skip){

    var low;
    var high;
    var skip;
    
    if (!skip) 
    {
        skip = 1;
    }
    if (!low) 
    {
        low = 0;
    }
    if (!high)
    { 
        high = low;
        low = 0;
    }
    for ( i= low; i < high; i= i + skip ){
    
     console.log( i);
    
    }
    }
    printRange(-122,22,2);