# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


higher_number = 0 

for score in student_scores:
    if score > higher_number:
        higher_number = score

print (f"The highest score in the class is: {higher_number}")

