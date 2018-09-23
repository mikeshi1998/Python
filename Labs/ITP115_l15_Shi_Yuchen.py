# Yuchen Shi
# ITP115, Spring 2018
# Lab L15
# yuchensh@usc.edu

MAX_COURSES = 6

class Student(object):
    def __init__(self, studentName, studentID):
        self.__name=studentName
        self.__idNumber=studentID
        self.__courses=[]

    def getName(self):
        return self.__name

    def setName(self, newName):
        if newName != "":
            self.__name=newName
        else:
            print("Invalid Name.")

    def getID(self):
        return self.__idNumber

    def setID(self, newID):
        self.__idNumber=newID

    def getCourses(self):
        return self.__courses

    def getNumberOfCourses(self):
        return len(self.__courses)

    def addCourse(self, newCourse):
        if self.getNumberOfCourses()<MAX_COURSES:
            self.__courses.append(newCourse)
            print("Course registration successful.")
        else:
            print("Course registration failed. This student has reached the maximum number of courses.")


    def __str__(self):
        msg="Student: "+self.__name+", ID: "+ str(self.__idNumber) +" enrolled in "+ str(self.getNumberOfCourses()) + " courses:"
        for course in self.__courses:
            msg += "\n\t- " + course
        return msg

def printStudents(studentList):
    print("\nStudents:")
    for student in studentList:
        print("\t" + str(studentList.index(student)+1) + ") " + student.getName())

def main():
    print("Welcome to the student registration system! ")
    s1=Student("Tiffany", 40)
    s2=Student("Isaaca", 41)
    s3=Student("Huy", 42)
    s4=Student("Brandon", 43)
    studentList=[s1, s2, s3, s4]

    goOn="y"
    while goOn.lower()=="y":
        printStudents(studentList)
        studentOption=int(input("Select a student from the list (1-4): "))
        while studentOption not in [1, 2, 3, 4]:
            studentOption=int(input("Invalid option. Please try again. "))
        newCourse=input("Enter the course the student is registering for: ")
        studentList[studentOption-1].addCourse(newCourse)
        goOn=input("Would you like to continue registering? (y/n): ")

    print()
    print(s1)
    print(s2)
    print(s3)
    print(s4)

main()