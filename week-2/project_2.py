name_1 = str(input("Enter first name: "))
name_2 = str(input("Enter second name: "))

age_1 = int(input("Enter age of name 1: "))
age_2 = int(input("Enter age of name 2: "))

def swap_ages(age_1, age_2):
 temp = age_1 # store the first age in temp 
 age_1 = age_2
 age_2 = temp
 return age_1, age_2 

age_1, age_2 = swap_ages(age_1, age_2)

print(f"The age of name_1 after swapping is {age_1}")
print(f"The age of name_2 after swapping is {age_2}")
