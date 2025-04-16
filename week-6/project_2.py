# Create lists to store admitted and not admitted and not admitted candidates
admitted = []
not_admitted = []

# Funcion to check admission
def check_admission(name, department, jamb_score, credits, interview_passed):
    if department == "Computer science":
        if jamb_score >= 250 and credits >= 5 and interview_passed:
            admitted.append(name)
            print(name, "has been admitted into Computer science.")
        else:
            not_admitted.append(name)
            print(name, "was not admitted into Computer science.")
    elif department == "Mass Communication":
        if jamb_score >= 230 and credits >= 5 and interview_passed:
            admitted.append(name)
            print(name, "has been admitted into Mass Communication")
        else:
            not_admitted.append(name)
            print(name, "was not admitted into Mass Communication.")
    else:
        print("Invalid department selected")

# Ask how many candidates to check
num = int(input("How many candidates do you want to check"))

# Loop to collect info for each candidate
for i in range(num):
    print("\nEnter information for candidates", i+1)
    name = input("Name: ")
    department = input("Department (Computer Science or Mass Communication):")
    jamb_score = int(input("JAMB Score: "))
    credits = int(input("Number of credits in 5 key subjects: "))
    interview_input = input("Did the candidate pass the interview? (yes or no): ")
    interview_passed = interview_input.lower() == "yes"

    check_admission(name, department, jamb_score, credits, interview_passed)

# Show array
print("Admitted candidates:", admitted)
print("Not admitted candidates:", not_admitted)
