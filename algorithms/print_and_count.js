/*from low num to high num
check num % 5 === 0
{
counter++
console.log(num)}
print counter*/



function divisibleByFive(low,high){
var num = low;
var counter=0;
var high;

while (num <= high){


    if(num % 5 === 0){

        console.log(num);
        num++;
        counter++;

    }
    else { num++;
    }
} 
console.log(counter);
}

divisibleByFive(512,4096);