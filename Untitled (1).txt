#Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.

class Student:

  def __init__(self, name, rollno, cgpa):
    self.name = name
    self.rollno = rollno
    self.cgpa = cgpa

def sort_students(student_list):
  sorted_students = sorted(student_list, key = lambda student : student.cgpa, reverse = True)
  return sorted_students

student = [ Student("Amoka","A01",9.1), Student("Praveen","A02",9.9), Student("Pooja","A03",7.8), Student("Yoga Dharshini","A04",8.9) ]

sorted_students = sort_students(student)

for student in sorted_students:
  print("Name: {}, Rollno: {}, CGPA: {}".format(student.name, student.rollno, student.cgpa))