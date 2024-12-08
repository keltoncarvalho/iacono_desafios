# Case 1: Breaking loop in the middle of execution
print('Primeiro loop')
i = 1 # Initializing counter
while i <= 10: # Loop with stop condition at 10
    if i == 5: # Condition for break clause
        print(i)
        break # Break clause
    else:
        print(i)
        i += 1

print('Segundo loop')
i = 1
while i <= 10:
    if i == 5: # if statement will increment the counter but skip the print when i=5
        i += 1
        continue
    else:
        print(i)
        i += 1
        