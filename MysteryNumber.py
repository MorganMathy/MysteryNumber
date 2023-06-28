import random

number_to_guess = random.randint(0, 100)
max_attempts = 5
number_input = None

for attempt in range(1, max_attempts + 1):
    try:
        number_input = int(input('Essayez de trouver le nombre mystère : '))
    except ValueError:
        print('Veuillez entrer un nombre valide.')
        continue

    if number_input == number_to_guess:
        print(f'Bravo, vous avez trouvé le nombre mystère ! C\'était {number_to_guess}. Vous l\'avez trouvé en {attempt} coup(s) !')
        break
    elif number_input > number_to_guess:
        print('Le nombre mystère est plus petit.')
    else:
        print('Le nombre mystère est plus grand.')

if number_input is None or number_input != number_to_guess:
    print(f'Vous avez perdu. Le nombre mystère était {number_to_guess}.')
