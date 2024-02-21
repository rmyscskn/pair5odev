from student import Student
from teacher import Teacher

öğrenciler = []
öğretmenler = []

def addStudent(name, lastName, sNumber):
    newStudent = Student(name,lastName,sNumber)
    öğrenciler.append(newStudent)
 
def addTeacher(name,lastName,branch):
    newTeacher = Teacher(name,lastName,branch)
    öğretmenler.append(newTeacher)

def resultStudents():
    for student in öğrenciler:
        print(student.information())
    
def resultTeachers():
    for teacher in öğretmenler:
        print(teacher.information())
    
addStudent("Yasemin","Karasakal",9)
addStudent("Rümeysa","Coşkun",4444)
addStudent("Süleyman","Kulaksız",23)
addTeacher("Hülya","Gökdemir","Matematik")
addTeacher("Abdullah","Keskin","Mutlu Olmak İstiyor")
addTeacher("Meryem","Özgün","Fizik")

resultStudents()
resultTeachers()



