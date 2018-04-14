/*var students = [ 
    {first_name:  'Michael', last_name : 'Jordan'},
    {first_name : 'John', last_name : 'Rosales'},
    {first_name : 'Mark', last_name : 'Guillen'},
    {first_name : 'KB', last_name : 'Tonel'}
];
for (var i= 0; i <= students.length-1; i++){


       console.log(students[i].first_name + " " +students[i].last_name);

}*/

var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
     ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
     ]
    }


   
    /*for (const [key, value] of Object.entries(users)) {
      console.log(`${key} ${value}`); 
    }*/



    Object.entries(users).forEach(([key, value]) => {
        console.log(`${key} ${value}`); 
        });



/*var text ="";
var x;
   for (x in users){
       console.log(x);
        
       text += users[x];
       console.log(text);
   }
   /*for (var i = 0; i< users.text.length; i++){
            var string1 = users.text[i].first_name ;
            var string2 = users.text[i].last_name;
            var sln = string1.length + string2.length;
            console.log(i+1 + " " + users.text[i].first_name + " " + users.text[i].last_name + " " +sln);   }
   }*/