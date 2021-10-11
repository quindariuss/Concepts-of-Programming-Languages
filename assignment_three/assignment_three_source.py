

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
course_test = Course("Math", 2102,"W02", "Fall", 2022, 35)

Courses.append(course_test)
print(Courses[0].name)

argument = ''

while argument != 'exit':
    argument = input("What would you like to do, or enter exit to cancel")

