years_of_experience = int(input("Enter your years of experience: "))

age = int(input("Enter your age: "))

if years_of_experience > 25 and age >= 55:
    print(f"Annual tax revenue(ATR) is: 5600000")
elif years_of_experience > 20 and age >= 45:
    print(f"Annual Tax Revenue(ATR) is: 4480000")
elif years_of_experience > 10 and age >= 35:
    print(f"Annual Tax Revenue(ATR) is: 1500000")
else:
    print(f"Annual Tax Revenue(ATR) is: 550000")