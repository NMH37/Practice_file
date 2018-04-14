


var hour = 7;
var minutes = 15;
var period = "AM";


if (( period === "AM") && ( hour < 8))
{
  
  if ( minutes < 15){
    console.log(" it is just " +  hour + "in the morning" );
  }
  if (minutes == 45){
      var almost = hour+1;
      cosole.log("it is quarter to " + almost );
  }
  if (minutes >= 55){
    var  almost= hour +1;
      console.log(" it is almost " +  almost + "in the morning" );
  }

} 
//else if ((period == AM) &&( hour > 8))
//{ console.log(" Wake up! it is "+ hour + minutes + "in the morning. You are getting late for work");
//}










