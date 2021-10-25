# Creating a Course Object
class Course: 
    def __init__(self, name, number, section, term, year, student_count):
        self.name = name 
        self.number = number 
        self.section = section 
        self.term = term 
        self.year = year 
        self.sudent_count = student_count

# Defining an array of courses
Courses = []
course_test = Course("Math", "2102","W02", "Fall", "2022", "35")

# Adding a test course
Courses.append(course_test)

# Variable to be used as an argument passer
argument = ''
print(
        """
┌──────────────────────────────────────┐
│     ____                             │
│    / ___|___  _   _ _ __ ___  ___    │
│   | |   / _ \| | | | '__/ __|/ _ \   │
│   | |__| (_) | |_| | |  \__ \  __/   │
│    \____\___/ \__,_|_|  |___/\___|   │
│                                      │
│        _       _     _               │
│       / \   __| | __| | ___ _ __     │
│      / _ \ / _` |/ _` |/ _ \ '__|    │
│     / ___ \ (_| | (_| |  __/ |       │
│    /_/   \_\__,_|\__,_|\___|_|       │
│                                      │
└──────────────────────────────────────┘
    Description:
        Allows you to add and
        manage your courses the way you
        like em!

Commands:

    add         starts interactive prompt for adding a new course

    list        shows all the courses in the program

    change      starts interactive prompt to change a course attributes

    exit        exits the command prompt

""")
# Exit Control Flow 
while argument != 'exit':
    argument = input(
    """
~~Course Adder~~ 
    """)
    # If Statements to parse the argument variable 
    if argument == 'add':
        course_to_add = Course(input("What is the name of the course?"), input("Course Number"),input("Section"), input("Term"), input("Year"), input("Students"))
        Courses.append(course_to_add);
        print(
              """
                      Added Course
              ||||||||||||||||||||||||||||
                         %s %s 
                 Section %s of %s %s
              ||||||||||||||||||||||||||||
              """ % (course_to_add.name, course_to_add.number, course_to_add.section, course_to_add.term, course_to_add.year)
              )
    elif argument == 'list':
        for index in range(0, len(Courses)):
            print(
                    """
                    Index: %i
                    ||||||||||||||||||||||||||||
                               %s %s 
                       Section %s of %s %s
                    ||||||||||||||||||||||||||||
                    """ % (index,Courses[index].name, Courses[index].number, Courses[index].section, Courses[index].term, Courses[index].year)
                    )
    elif argument == 'change':
       course_to_change_input = input("Whats the index of the course you would like to change: ")
       course_to_change = Courses[int(course_to_change_input)] 
       course_changer = input("What value would you like to change: ")
       while course_changer != 'done':
           if course_changer == 'name':
               course_to_change.name = input("New Name: ") 
               print('Changing name')
           elif course_changer == 'number':
               course_to_change.number = input("New Number: ") 
               print('Changing name')
           elif course_changer == 'section':
               course_to_change.section =  input("New Section: ") 

               print('Changing name')
           elif course_changer == 'year':
               course_to_change.year =  input("New Year: ") 

               print('Changing name')
           elif course_changer == 'term':
               course_to_change.term =  input("New Term: ") 

               print('Changing name')
           elif course_changer == 'students':
                course_to_change.student_count =  input("New Student Count: ") 

                print('Changing name')
           course_changer = input("What other value would you like to change?")
            
    elif argument == 'exit':
        print('Logging off...')
    else :
        print('That is not a command, here is a reminder: ')
        print("""
Commands:

    add         starts interactive prompt for adding a new course

    list        shows all the courses in the program

    change      starts interactive prompt to change a course attributes

    exit        exits the command prompt
        """
        ) 
