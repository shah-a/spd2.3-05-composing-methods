"""Exercise 6: Extract Function and Replace Temp with Query"""


class Employer:
    def __init__(self, name):
        self.name = name

    def send(self):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students
        self.min_gpa = 2.5  # minimum acceptable GPA

    def get_passing_students(self):
        return [s for s in self.students if s.get_gpa() > self.min_gpa]

    def print_passed_students(self, passed_students):
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')

    def get_top_10_percent(self, passed_students):
        passed_students.sort(key=lambda s: s.get_gpa())
        index = int(0.9 * len(passed_students))
        return passed_students[index:]

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passed_students = self.get_passing_students()

        # print student's name who graduated.
        self.print_passed_students(passed_students)

        # Send congrat emails to them.
        for s in passed_students:
            s.send_congrat_email()

        # Find the top 10% of them and send their contact to the top employers
        top_10_percent = self.get_top_10_percent(passed_students)

        top_employers = [Employer('Microsoft'), Employer(
            'Free Software Foundation'), Employer('Google')]

        for e in top_employers:
            e.send(top_10_percent)


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]
school = School(students)
school.process_graduation()
