
class Student:
    
    __slots__ = ["id", "name", "gpa", "credits", "courses"]
    # slots basically say you cant make anything that arent these. 

    # Static Fields - Belong to the CLASS, NOT to the object
    # id = "No I.D."
    # name = "No name"
    # gpa = 0.0
    # credits = 0   
    # courses = []   # If you do this then EVERY student will have the same courses because it is a static (GLOBAL) variable for ALL students.

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.gpa = 0.0
        self.credits = 0
        self.courses = []     # Put it here.

       
def print_student(student):
    print("ID: ", student.id, "\nName: ", student.name, "\nGPA: ", student.gpa, "\nCredits: ", student.credits, "\nCourses: ", student.courses, sep = "")
    print()

def main():
    student1 = Student("cmm2729", "Christian Morgado")
    # student1.id = "cmm2729"
    # student1.name = "Christian Morgado"
    student1.gpa = 4.0
    student1.credits = 9437
    student1.courses.append("SWEN-101")
    student1.courses.append("GCIS-123")
    print_student(student1)

    student2 = Student(0, 0)
    student2.courses.append("NSSA-102")
    student2.courses.append("ISTE-140")

    print_student(student2)

if __name__ == "__main__":
    main()
