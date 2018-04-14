
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'guillen'},
     {'first_name' : 'KB', 'last_name' : 'tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'michael', 'last_name' : 'choi'},
     {'first_name' : 'martin', 'last_name' : 'puryear'}
  ]
 }

def show_students(arr):
    for index in students:
        print index['first_name'], index['last_name']
#show_students(students)

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)
show_all(users)

# MY VERSION TO UNDERSTAND !
def show_all_users(users):
    for rank in users:
        counter = 0
        print rank
        for human in users[rank]:
            counter +=1
            Full_name = human["first_name"]+human["last_name"]
            length = len(Full_name)
            print counter,human["first_name"],human["last_name"],length

#show_all_users(users)