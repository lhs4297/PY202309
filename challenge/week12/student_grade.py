from Student import *


def main():
    file_path = 'student.csv'  # file path

    # load student data
    students = loadData(file_path)

    # Output the students' average scores
    print("-----학생들의 평균 점수-----")
    for student in students:  # Calculate the average score for each student
        average_score = student.get_average() 
        print(f"{student.name}의 평균 점수는 {average_score} 입니다.")  # Average Score Output

    # Save the average score to a file
    with open('average.txt', 'w', encoding='utf-8') as output_file:  # Open a file
        output_file.write("-----학생들의 평균 점수-----\n")  # Writing Headers
        for student in students:  # Calculate the average score for each student
            average_score = student.get_average()
            output_file.write(f"{student.name}의 평균 점수는 {average_score} 입니다.\n")  # Write an average score


if __name__ == "__main__":
    main()