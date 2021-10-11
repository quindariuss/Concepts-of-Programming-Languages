

# Change a Course Object 

# Store the Course Object 

# Show all the values for the courses

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

Courses.append(course_test)
print(Courses[0].name)

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
while argument != 'exit':
    argument = input(
    """
~~Course Adder~~ 
    """)
    if argument == 'add':
        print('Add function')
    elif argument == 'list':
        for index in range(0, len(Courses)):
            print(
                    """
                    ||||||||||||||||||||||||||||
                               %s %s 
                       Section %s of %s %s
                    ||||||||||||||||||||||||||||
                    """ % (Courses[index].name, Courses[index].number, Courses[index].section, Courses[index].term, Courses[index].year)

                    )
    elif argument == 'change':
       course_to_change = input("Whats the number of the course you would like to change")
       course_changer = input("What value would you like to change")
       while course_changer != 'done':
           course_changer = input("What else")
           if course_changer == 'name':
                print('Changing name')
           elif course_changer == 'number':
               print('Changing name')
           elif course_changer == 'section':
               print('Changing name')
           elif course_changer == 'year':
               print('Changing name')
           elif course_changer == 'term':
               print('Changing name')
           elif course_changer == 'students':
                print('Changing name')
            
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

def list():
    print('hello')

