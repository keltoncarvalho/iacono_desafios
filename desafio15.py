# Creating the list
frutas = ['maçã', 'maçã', 'maçã', 'melancia', 'maçã', 'goiaba', 'goiaba']

count = 0 # initializing counter
for fruta in frutas: # looping through list
    if fruta == 'maçã': # condition
        count += 1 # increment if condition is True

# printing the result
print(f'A lista possui {count} maçãs') 
