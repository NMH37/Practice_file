

function fancyArray(arr,fancy){

    for ( i = 0; i< arr.length; i++){

         console.log( i + fancy + arr[i]);

    }
}

var fancy= "-->";
var arr = ["james","jack","ron"];
fancyArray(arr, fancy);