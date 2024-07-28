# define the dictionaries
class_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

class_faculty = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

class_schedule = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# def to display class details
def display_class_details(class_number):
    if class_number in class_rooms and class_number in class_faculty and class_number in class_schedule:
        print(f"Class Number: {class_number}")
        print(f"Class Room Number: {class_rooms[class_number]}")
        print(f"Faculty: {class_faculty[class_number]}")
        print(f"Scheduled meeting time: {class_schedule[class_number]}")
    else:
        print("Class not found.")

# prompt the user for the class number and display the class details
class_number = input("Enter a course number: ").strip()
display_class_details(class_number)