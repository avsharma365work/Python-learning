# Smart study Planner
import matplotlib.pyplot as plt

print("====================My Smart Study Buddy====================")


# Thoda introduction to banta hai na student ka
name = input("Enter your lovely name: ")
study = input("Enter your class or course: ")

# This is menu options mechanism by using class and object oriented programming
class smart_study_planner:
    def __init__(self):
        self.add_subjects = []
        self.mark_add = {}


    def add_subject(self):
        self.subjects = input("Enter the subject you want to add: ")
        self.add_subjects.append(self.subjects)
        print("Subject added successfully!")

    # Basically marks add krne ke liye
    def add_marks(self):
        for i, j in enumerate(self.add_subjects, 1):
            print(f"{i}. {j}")
        self.choice = int(input("Enter the subject serial which you want to add marks for: "))
        n = 1

        if self.add_subjects[self.choice - 1] not in self.mark_add:
            self.mark_add[self.add_subjects[self.choice - 1]] = []
        while n <= 3:
            self.marks = int(input(f"Enter the marks of {self.add_subjects[self.choice - 1]} exam {n} (MIN 3): "))
            n += 1
            self.mark_add[self.add_subjects[self.choice - 1]].append(self.marks)
            print("Marks added successfully!")

    # Marks display karne ke liye
    def display(self):
        print("Subjects and Marks:")
        for k, v in self.mark_add.items():
            print(f"Subject {k} and Marks {sum(v)}")

    def performance_analysis(self):
        for k, v in self.mark_add.items():
            if sum(self.mark_add[k]) >= 150:
                print(f"Subject {k} and Performance is Excellent")
            elif sum(self.mark_add[k]) >= 100:
                print(f"Subject {k} and Performance is Good")
            elif sum(self.mark_add[k]) >= 75:
                print(f"Subject {k} and Performance is Average")
            else:
                print(f"Subject {k} and Performance is Poor")

        # Thode visuals ke liye only basic of matplotlib use kiya hai

        plt.plot(self.add_subjects, self.mark_add.values())
        plt.xlabel("Subjects", fontweight="bold")
        plt.ylabel("Marks", fontweight="bold")
        plt.title("Overall Performance", color="olive", fontweight="bold")
        plt.show()

        plt.bar(self.add_subjects, [sum(i) for i in self.mark_add.values()])
        plt.xlabel("Subjects", fontweight="bold")
        plt.ylabel("Marks", fontweight="bold")
        plt.title("Overall Performance", color="olive", fontweight="bold")
        plt.show()

    # Sabse se important time management ke liye
    def time_manage(self):
        self.study_time = float(input("Enter your Focus on study time(in Minutes): "))
        print(f"your total study time is {self.study_time}")
        print(f"Given study time on each subjects is {self.study_time / len(self.add_subjects)}minutes")
        # creating table
        print("++++++++++Basic Advice for You+++++++++++")
        print('-' * 50)
        self.msg = [
            "Now you enter real world",
            "Give extra time on your core/major subjects",
            "Give more effort on weak subjects"]

        for m, n in enumerate(self.msg, 1):
            print(m, n)
        print('-' * 50)
        # Creating basic table
        print('-' * 50)
        print(f"{'Subject':<15}{'Marks':<20}{'Total':<10}")
        print('-' * 50)
        for i, j in self.mark_add.items():
            print(f"{i:<15}{str(j):<20}{sum(j):<10}")
            print('-' * 50)




a = smart_study_planner()
# Main logic or menu yaha se banega...

print("Hello", name)
print("How are you Buddy....")
print("1, Add Subjects")
print("2. Add Marks")
print("3. Display Data")
print("4. Performance Analyzing")
print("5. Advice for Time Management")
print("6. Exit")
while True:
    # Conditional statements for choicing
    choice = int(input("Enter your option(1-6): "))
    if choice == 1:
        a.add_subject()
    elif choice == 2:
        a.add_marks()
    elif choice == 3:
        a.display()
    elif choice == 4:
        a.performance_analysis()
    elif choice == 5:
        a.time_manage()
    elif choice == 6:
        print("Thankyu yaar")
        print("Bye!,I think you enjoy")
        break
    else:
        print("Oh!,I think you choose invalid choice")
















