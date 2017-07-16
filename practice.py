"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""

class Student(object):
    """A student"""

    def __init__(self, first_name, last_name, address):
        """Initialize student"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question(object):
    """Questions"""

    def __init__(self, question, correct_answer):
        """Initialize questions"""

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Prompts user for answer to question and evaluates"""

        if raw_input(self.question + " > ") == self.correct_answer:
            return True
        else:
            return False


class Exam(Question):
    """Exams"""

    def __init__(self, name):
        """Initialize exam"""

        self.name = name
        self.questions = []

    def add_question(self, question):
        """Adds a question to the list of exam questions"""
        self.questions.append(question)

    def administer(self):
        """Administers exam"""

        correct_counter = 0.0
        question_counter = 0.0

        for question in self.questions:
            result = question.ask_and_evaluate()
            question_counter += 1
            if result == True:
                correct_counter += 1

        score =  correct_counter / question_counter
        return score

# class StudentExam(Exam):
#     """Student Exam"""

#     def __init__(self, student, exam):
#         """Initialize student exam"""

#         super(StudentExam, self).__init__(name)

#         self.student = student
#         self.exam = exam
#         self.score = None

#     def take_test(self):
#         """Take exam"""

#         score = super(StudentExam, self).administer()
#         print score

# def example():
#     """Example of functionality"""

#     # creates an exam
#     example = Exam('midterm')

#     # initialize questions
#     question_1 = Question('What is my cats name?', 'Hellboy')
#     question_2 = Question('How cute is she?', 'VERY')
#     question_3 = Question('Which Persona am I playing?', '5')

#     # add a few questions to the exam
#     example.add_question(question_1)
#     example.add_question(question_2)
#     example.add_question(question_3)

#     # create a student
#     kitty_student = Student('Hellboy','ORourke','953 Pacific Ave')

#     # instantiate a StudentExam, passing the student and exam you just created as arguments
#     test_exam = StudentExam(kitty_student, example)

#     # Administers the test for that student using the take_test method you just wrote
#     test_exam.take_test()

# example()




