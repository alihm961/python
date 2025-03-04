class Student:  #Class representing a single student
    def __init__(self, name, grade):      #Constructor to initialize student name and grade
        self.name = name      
        self.grade = grade
    
    def display_info(self):   #Method to display students name and grade
        print(f"Student: {self.name}, Grade: {self.grade}")
        
class GradeManager:  #Class managing multiple students and their grades
    def __init__(self):
        self.students = []  # List to store student objects
        
    def add_student(self, name, grade):  # Adds a new student object to the list
        student = Student(name, grade) # Create a new student instance
        self.students.append(student)  # Add the student to the list
        
    def display_students(self):  # Displays all students and their grades
        if not self.students:
            print("No students added yet!")
            return
        print("Student List: ")
        for student in self.students:
            student.display_info()  # Calls Student class method to display info
            
    def calculate_average(self):
        if  not self.students:
            print("No students to calculate average!")
            return
        
        total_grades = sum(student.grade for student in self.students) #sum of all grades
        average = total_grades / len(self.students)  # Calculate average
        print(f"Class average grade: {average:.2f}")  # Display average
        
def main():
    manager = GradeManager()  # Create an instance of GradeManager
    
    while True:
        print("\nStudent Grade Manager")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Class Average")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            
            while True:
                try:
                    grade = float(input("Enter student grade: "))
                    break
                except ValueError:
                    print("Invalid grade! Please enter a number.")
                    
            manager.add_student(name, grade)
            
        elif choice == "2":
            manager.display_students()
            
        elif choice == "3":
            manager.calculate_average()
            
        elif choice == "4":
            print("Goodbye! Have a good day!")
            break
        
        else:
            print("Invalid option! please try again.")
            
        
if __name__ == "__main__":
    main()
        