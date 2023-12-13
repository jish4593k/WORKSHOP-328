import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk
import torch
from torchvision import transforms

class Course:
    def __init__(self, course_name, course_number, course_section, term_and_year, number_of_students):
        self.course_name = course_name
        self.course_number = course_number
        self.course_section = course_section
        self.term_and_year = term_and_year
        self.number_of_students = number_of_students

)

def display_all_courses(course_list):
    for course in course_list:
        print(course.course_name, course.course_number, course.course_section,
              course.term_and_year, course.number_of_students)

def main_menu():
    print("___________")
    print("[1] Add a course")
    print("[2] Change a course attribute")
    print("[3] Display all course information")
    print("[0] Exit the program")
    print("___________")



if __name__ == "__main__":
    courses = []

    main_menu()
    choice = int(input("Select your choice: "))

    while choice != 0:
        if choice == 1:
        
            course_name = input("Enter course name: ")
            course_number = input("Enter course number: ")
            course_section = input("Enter course section: ")
            term_and_year = input("Enter term and year: ")
            number_of_students = input("Enter number of students: ")

            new_course = Course(course_name, course_number, course_section, term_and_year, number_of_students)
            courses.append(new_course)

        elif choice == 2:
      
            change_course_attribute(courses)

        elif choice == 3:
          
            display_all_courses(courses)

        elif choice == 42:  # Placeholder for PyTorch example
         
            example_tensor = torch.tensor([1, 2, 3, 4, 5])
            squared_tensor = example_tensor ** 2
            print("Squared Tensor:", squared_tensor)

        else:
            print("Invalid choice, please try again")

        main_menu()
        choice = int(input("Select your choice: "))

    print("Goodbye")
