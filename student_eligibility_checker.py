import numpy as np

students = np.array([
    ["Aarav", 6.5, 35],
    ["Ishaan", 7.2, 40],
    ["Prisha", 5.8, 38],
    ["Vihaan", 6.0, 20],
    ["Ananya", 8.0, 45],
    ["Arjun", 6.3, 30],
    ["Saanvi", 7.0, 48],
    ["Rohan", 5.2, 25],
    ["Neha", 6.8, 39],
    ["Kavya", 5.9, 22],
    ["Dev", 7.5, 46],
    ["Ria", 4.8, 33],
    ["Aditi", 8.2, 42],
    ["Shiv", 6.1, 28],
    ["Nikhil", 7.8, 44],
    ["Tanvi", 6.4, 30],
    ["Siddharth", 5.7, 20],
    ["Ayaan", 6.0, 35],
    ["Meera", 8.5, 48],
    ["Arnav", 5.6, 24],
], dtype=object)

names = students[:, 0]
cgpa = students[:, 1].astype(float)
assessment_scores = students[:, 2].astype(float)
assessment_percentages = (assessment_scores / 50) * 100

# Eligibility criteria: CGPA >= 5.0 and assessment percentage >= 75%
eligibility = (cgpa >= 5.0) & (assessment_percentages >= 75)

# Selection criteria: eligible and assessment percentage >= 80% for interview
interview_selection = eligibility & (assessment_percentages >= 80)

print("Eligibility and Interview Selection Results for 20 Students:")
print("-" * 80)
for i, name in enumerate(names):
    eligibility_status = "Eligible" if eligibility[i] else "Not Eligible"
    interview_status = "Selected for Interview" if interview_selection[i] else "Not Selected for Interview"
    print(f"{name}: CGPA = {cgpa[i]:.1f}, Assessment = {assessment_percentages[i]:.2f}%, "
          f"Eligibility = {eligibility_status}, Interview Status = {interview_status}")
