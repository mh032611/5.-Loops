#For Loop and the Range Function

for number in range (1, 11, 3):
  print(number)
# 3 is a step-into number. counts by 3
# 1, 4, 7, 10 

total = 0
for number in range(1, 101):
  total += number
print(total)