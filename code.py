class EDiaryWithAllFeatures:
    all_students = []

    def _init_(self, student_name):
        self.student_name = student_name
        self.subjects = {}
        self.rating_points = 0
        self.achievements = []
        self.comments = {}
        EDiaryWithAllFeatures.all_students.append(self)

    def add_grade(self, subject, grade):
        if subject in self.subjects:
            self.subjects[subject].append(grade)
        else:
            self.subjects[subject] = [grade]
        self.update_rating()

    def add_achievement(self, achievement):
        self.achievements.append(achievement)

    def add_comment(self, subject, comment):
        if subject in self.comments:
            self.comments[subject].append(comment)
        else:
            self.comments[subject] = [comment]

    def update_rating(self):
        for subject, grades in self.subjects.items():
            for grade in grades:
                if grade >= 4:
                    self.rating_points += 1

    @staticmethod
    def calculate_overall_rating():
        all_ratings = [student.rating_points for student in EDiaryWithAllFeatures.all_students]
        all_ratings.sort(reverse=True)
        return all_ratings

    def check_bonus_eligibility(self):
        overall_rating = EDiaryWithAllFeatures.calculate_overall_rating()
        five_percent_threshold = int(0.05 * len(overall_rating))
        if self.rating_points >= overall_rating[:five_percent_threshold][-1]:
            return f"{self.student_name} receives a bonus for maintaining 5% of the highest rating!"
        else:
            return f"{self.student_name} does not hold the highest 5% rating."

    def view_grades(self):
        print(f"Electronic journal for {self.student_name}:")
        for subject, grades in self.subjects.items():
            average_grade = sum(grades) / len(grades)
            print(f"{subject}: {grades}, Average grade: {average_grade:.2f}")

    def view_achievements(self):
        print(f"Achievements of student {self.student_name}:")
        for achievement in self.achievements:
            print(achievement)

    def view_comments(self):
        print(f"Comments for student {self.student_name}:")
        for subject, comments in self.comments.items():
            print(f"{subject}: {', '.join(comments)}")

# Usage example:
student1 = EDiaryWithAllFeatures("Ivanov Ivan")
student1.add_grade("Mathematics", 4)
student1.add_grade("Mathematics", 5)
student1.add_grade("Physics", 3)
student1.add_grade("Physics", 4)
student1.add_achievement("Winner of the Math Olympiad")
student1.add_comment("Math", "Great job!")

student2 = EDiaryWithAllFeatures("Petrov Peter")
student2.add_grade("Mathematics", 5)
student2.add_grade("Mathematics", 4)
student2.add_grade("Physics", 5)
student2.add_grade("Physics", 4)
student2.add_achievement("Best progress in class")
student2.add_comment("Physics", "Well done!")

student1.view_grades()
student1.view_achievements()
student1.view_comments()

student2.view_grades()
student2.view_achievements()
student2.view_comments()

print(student1.check_bonus_eligibility())
print(student2.check_bonus_eligibility())
