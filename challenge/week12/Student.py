# Define Student Classes
class Student:
    # Producer function: Initialize by inputting name, Korean, math, and English scores
    def __init__(self, name, korean, math, english):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english

    # Method of calculating and returning average scores
    def get_average(self):
        return (self.korean + self.math + self.english) / 3

# A function that reads data from a file and creates a Student object and stores it in a list
def loadData(file_path):
    data = []   # Create a blank list to store student data
    with open(file_path, 'r', encoding='utf-8') as file:   # Open a file
        lines = file.readlines()   # Read each line of the file and save it as a list
        for line in lines[1:]:   # For each line except the header, separate lines with commas and convert them to a list
            elements = line.strip().split(',')
            name = elements[0]  
            scores = list(map(float, elements[1:]))   # The remaining factors are points (converted to real type)
            student = Student(name, scores[0], scores[1], scores[2])   # Create Student Object
            data.append(student)   # Adding Student Objects to the List
    return data   # Return student data list
