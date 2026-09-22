# Academic Performance Prediction System

print("======================================")
print("   ACADEMIC PERFORMANCE PREDICTION")
print("======================================")

# Taking student details
name = input("Enter student name: ")

marks = float(input("Enter average marks (out of 100): "))
attendance = float(input("Enter attendance percentage: "))
study_hours = float(input("Enter average study hours per day: "))
previous_cgpa = float(input("Enter previous CGPA (out of 10): "))

# Calculate performance score
score = (
    (marks * 0.50) +
    (attendance * 0.20) +
    (study_hours * 5 * 0.15) +
    (previous_cgpa * 10 * 0.15)
)

# Prediction
if score >= 85:
    performance = "Excellent"
    prediction = "Very High Performance"
elif score >= 70:
    performance = "Good"
    prediction = "High Performance"
elif score >= 55:
    performance = "Average"
    prediction = "Moderate Performance"
else:
    performance = "Needs Improvement"
    prediction = "Low Performance"

# Display result
print("\n======================================")
print("        PERFORMANCE REPORT")
print("======================================")

print("Student Name:", name)
print("Average Marks:", marks)
print("Attendance:", attendance, "%")
print("Study Hours:", study_hours)
print("Previous CGPA:", previous_cgpa)
print("Performance Score:", round(score, 2))
print("Performance:", performance)
print("Prediction:", prediction)

# Suggestions
print("\nSuggestion:")

if performance == "Excellent":
    print("Keep up the good work and maintain your performance.")
elif performance == "Good":
    print("Continue regular studies and try to improve weak subjects.")
elif performance == "Average":
    print("Increase study hours and focus on attendance and difficult subjects.")
else:
    print("Follow a proper study schedule and seek help from teachers.")

print("======================================")