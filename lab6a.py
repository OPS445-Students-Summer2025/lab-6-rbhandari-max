#!/usr/bin/env python3
# Author ID:rbhandari172myseneca.ca

class Student:
    """
    Student class to store and manage student information and grades.
    Attributes:
        name (str): The student's name.
        number (str): The student's ID number as a string.
        courses (dict): A dictionary mapping course names to grades.
    """

    def __init__(self, name, number):
        """
        Initializes a Student object with a name, ID number, and empty courses dictionary.
        Converts number to string to avoid TypeError in displayStudent.
        """
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        """
        Returns a formatted string with student name and number.
        """
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        """
        Adds or updates a grade for a given course in the student's record.
        """
        self.courses[course] = grade

    def displayGPA(self):
        """
        Calculates and returns the student's GPA.
        Handles case with no courses or zero division by returning 0.0 GPA.
        """
        if not self.courses:
            return 'GPA of student ' + self.name + ' is 0.0'

        total = 0.0
        count = 0
        for course in self.courses:
            total += self.courses[course]
            count += 1

        if count == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        else:
            gpa = total / count
            return 'GPA of student ' + self.name + ' is ' + str(gpa)

    def displayCourses(self):
        """
        Returns a list of courses the student has passed (grade > 0.0).
        """
        passed_courses = []
        for course in self.courses:
            if self.courses[course] > 0.0:
                passed_courses.append(course)
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Note: integer ID to test str conversion
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
#!/usr/bin/env python3
# Author ID: [YOUR_SENECA_ID]

class Student:
    """
    Student class to store and manage student information and grades.
    Attributes:
        name (str): The student's name.
        number (str): The student's ID number as a string.
        courses (dict): A dictionary mapping course names to grades.
    """

    def __init__(self, name, number):
        """
        Initializes a Student object with a name, ID number, and empty courses dictionary.
        Converts number to string to avoid TypeError in displayStudent.
        """
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        """
        Returns a formatted string with student name and number.
        """
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        """
        Adds or updates a grade for a given course in the student's record.
        """
        self.courses[course] = grade

    def displayGPA(self):
        """
        Calculates and returns the student's GPA.
        Handles case with no courses or zero division by returning 0.0 GPA.
        """
        if not self.courses:
            return 'GPA of student ' + self.name + ' is 0.0'

        total = 0.0
        count = 0
        for course in self.courses:
            total += self.courses[course]
            count += 1

        if count == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        else:
            gpa = total / count
            return 'GPA of student ' + self.name + ' is ' + str(gpa)

    def displayCourses(self):
        """
        Returns a list of courses the student has passed (grade > 0.0).
        """
        passed_courses = []
        for course in self.courses:
            if self.courses[course] > 0.0:
                passed_courses.append(course)
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Note: integer ID to test str conversion
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Display information for student1 object
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2 object
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
