# Creating two lists
frutas = ['banana', 'maçã', 'goiaba', 'melão', 'morango']
vegetais = ['batata', 'feijão', 'brócolis', 'alface']

# Nested Loops
for fruta in frutas: # Looping through the first list
    for vegetal in vegetais: # Looping through the second list
        print(f'{fruta} e {vegetal}') # Printing the combinations
