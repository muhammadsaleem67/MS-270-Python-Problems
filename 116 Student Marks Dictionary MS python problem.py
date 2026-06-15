def analyze_marks(marks_dict):
    if not marks_dict:
        return 0
        
    # Calculate total marks and count of students
    total_marks = sum(marks_dict.values())
    student_count = len(marks_dict)
    
    # Calculate average
    average = total_marks / student_count
    return average
students = {
    "Babar": 85,
    "Saleem": 92,
    "Irfan": 78
}
print(f"Class Average: {analyze_marks(students)}") 
# Output: Class Average: 85.0
