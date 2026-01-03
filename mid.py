class StudentDatabase:
  student_list = []
  
  @classmethod
  def add_student(self,std):
    self.student_list.append(std)
  
  @classmethod    
  def show_all_students(self):
    for std in self.student_list:
      print(std.view_student_info())
  
  @classmethod
  def find_student_by_id(self,id):
    for std in self.student_list:
      if std.student_id == id:
        return std
        

class Student:
  s_id = 101
  def __init__(self,name,department):
    self.student_id = self.id_generator()
    self.name = name
    self.department = department
    self.is_enrolled = False
    Student.s_id += 1
    StudentDatabase.add_student(self)
  
  def enroll_student(self):
    if not self.is_enrolled:
      self.is_enrolled = True
    else:
      print(f"{self.name} is already enrolled.")
  
  def drop_student(self):
    if self.is_enrolled is True:
      self.is_enrolled = False
         
  def id_generator(self):
    st = f"S{self.s_id}"
    return st 
  
  def view_student_info(self):
     return f"ID: {self.student_id}, Name: {self.name}, Department: {self.department}, Enrollled: {self.is_enrolled}\n"


std1 = Student("Alice Smith","Computer Science")
std1.enroll_student()
std2 = Student("Bob Johnson","Mathematics")
std3 = Student("Charlie Lee","Physics")
std3.enroll_student()


while True:
  print("1. View All Students")
  print("2. Enroll Student")
  print("3. Drop Student")
  print("4. Exit")
  
  chc = int(input("Enter your choice: "))
  
  if chc == 1:
    StudentDatabase.show_all_students()
  elif chc == 2:
    name = input("Name: ")
    dept = input("Department: ")
    std = Student(name,dept)
    std.enroll_student()
    print(f"{name} of {dept} Department successfully enrolled.")
  elif chc == 3:
    id = input("Enter Student ID to drop: ")
    student = StudentDatabase.find_student_by_id(id)
    if student:
      student.drop_student()
    else:
      print("Student does not exit")
  elif chc == 4:
    print("Exiting the system.........")
    break
  
  
