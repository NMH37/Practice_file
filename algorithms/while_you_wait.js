

function birthdayCountDown(daysUntilMyBirthday){

var daysUntilMyBirthday ;

while ( daysUntilMyBirthday >= 0) {
         
     
    if (daysUntilMyBirthday === 0){

        console.log(" It is your birthday");
        console.log("♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*");
        console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
        console.log("*•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«");

       
        break;
    }


    else if ( daysUntilMyBirthday >= 5){
    
        console.log("Still " + daysUntilMyBirthday + " days till my birthday :(");
        
     }


    if ( daysUntilMyBirthday <= 4)
    {

        console.log(" It is almost here !! , only " + daysUntilMyBirthday + " days left :)");
        
    }
     daysUntilMyBirthday = daysUntilMyBirthday - 1;
}
}

birthdayCountDown(40);