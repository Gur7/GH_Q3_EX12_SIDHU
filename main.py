# if-elif-else statement
from pyscript import display, document


def students_classifications(e):
    document.getElementById('output').innerHTML = ''

    classification = float(document.getElementById('number1').value)

    if classification >= 100:
        display(f'No grade Higher than 100', target='output')
    elif classification >= 95:
        display(f'Bergamo 1', target='output')
    elif classification >= 91:
        display(f'Bergamo 2', target='output')
    elif classification >= 86:
        display(f'Bergamo 3', target='output')
    elif classification >= 75:
        display(f'Perugia 1', target='output')
    elif classification >= 65:
        display(f'Perugia 2', target='output')
    else:
        display(f'Invalid input', target='output')