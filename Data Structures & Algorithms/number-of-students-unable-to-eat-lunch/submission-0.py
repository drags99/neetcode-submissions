"""
problem:
circle, 0
square, 1
students in a queue, each want a 0 or 1
number of students = number of 0's and 1's

students are in a stack
    if they like the sandwich they will take it and leave the queue
    else they go to the end of the queue

repeat till none of the students want to take the top of the sandwich
    - if fail to distribute sandwich return len of students list
return the number of students that aren't able to eat

approach:
pop and append student list to requeue, 
pop student if they got the sandwich they want
sandwiches only pop

complexity:
number of students^2
"""
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:        
        for sandwich in sandwiches:
            # see if any student wants the sandwich
            student_line = len(students)
            print(f"student line {student_line}")
            num_students_asked = 0
            while num_students_asked <= student_line:
                student = students.pop(0)
                student_likes_sandwich = student == sandwich
                if student_likes_sandwich:
                    num_students_asked += 1
                    # get next sandwich and see who wants it
                    break
                else:
                    # send student to end of line and increase talley
                    students.append(student)
                    num_students_asked += 1
                    if num_students_asked == student_line:
                        return len(students)
            
        return len(students)















