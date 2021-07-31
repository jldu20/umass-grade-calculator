# Note: This follows the University of Massachusetts Amherst grading scale.
# https://www.umass.edu/registrar/sites/default/files/Grading%20System.pdf




def get_grade_scale():
    grade_scale = {}
    grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-","D+", "D", "F"]
    for letters in grades:
        letter_to_number = int(input("Enter the grade needed for a " + letters + ": "))
        grade_scale[letters] = letter_to_number
    return grade_scale


def grade_categories():
    num_categories = int(input("Enter how many categories your grades have: "))
    class_weight = {}
    for percentages in range(0, num_categories): 
        category_name = input("Enter category (test, quiz, homework etc: ")
        category_percent = int(input("Enter how much the category weighs in percent: "))
        class_weight[category_name] = category_percent
    return class_weight
    
def grade_needed(grade_scale, grade_categories, grade):
        target_grade = input("What letter grade are you aiming for in the class? ")
        grade_needed = grade_scale[target_grade]
        points_needed = grade_needed - grade
        if points_needed > 0:
            message_lower_grade = "You currently are at a " + grade + ". You need " + points_needed + "more points"
            return message_lower_grade
        else:
            message_upper_grade = "You are already at or above this letter grade"
            return message_upper_grade
    

def current_overall_grade(grade_categories):
    grade_list = []
    get_keys = grade_categories.keys()
    key_list = list(get_keys)
    total_grade = 0
    for key in key_list: 
        curr_grade = int(input("Please input your current grade for " + key + " "))
        calculate_grade = curr_grade * grade_categories[key] / 100
        grade_list.append(calculate_grade)
    for grade in grade_list:
        total_grade += grade
    return total_grade

def gpa_calculation_semester(): 
    class_grades = []
    num_credits = 0
    total_gpa_points = 0
    num_classes = int(input("Enter how many classes you are currently taking"))
    for classes in range(num_classes):
        grade = int(input("Enter your letter for class " + classes + ": "))
        credits = int(input("How many credits is this class?"))
        class_grades.append(grade * credits)
        num_credits += credits
    for credits in class_grades:
        total_gpa_points += credits
    gpa = total_gpa_points/ num_credits
    gpa = round(gpa,1)
    print("Your GPA for this semester is: " + gpa)
    return gpa
def gpa_calculation_semester_helper(gpa): 
    curr_gpa = gpa
    letter_to_number_grades = {0.0:"F",1.0:"D",1.3:"D+",1.7:"C-",2.0:"C",2.3:"C+",2.7:"B-",3.0:"B",3.3:"B+",3.7:"A-",4.0:"A"}
    while not gpa in letter_to_number_grades:
        curr_gpa = curr_gpa - 0.1
    letter_grade = letter_to_number_grades[curr_gpa]
    return letter_grade
def main():
    grade_scale = get_grade_scale()
    print(grade_scale)
    grade_cat = grade_categories()


if __name__ == '__main__':
    main()
