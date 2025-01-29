# Main data including income, expense and total stored in dict
data = {'income': [], 'expense': [],'total': 0 }

# Adding income to main data dict
def add_income():
    # Loop working untill user type correct input or press q/Q
    while True:
        income_input = input("Dodaj wpłatę (np. 100, 125.25) jeśli chczesz wyjść nacisnij 'w': ")
        if income_input.lower() == 'w': break
        if income_input.replace('.', '', 1).isdigit():
            income_input = float(income_input)
            data['income'].append(income_input)
            break
        else:
            print("Błąd: Kwota musi być liczbą.")
    
def add_expense():
    # Loop working untill user type correct input or press q/Q
    while True:
        expense_input = input("Dodaj wydatek (np. 100, 125.25) jeśli chczesz wyjść nacisnij 'w': ")
        if expense_input.lower() == 'w': break
        if expense_input.replace('.', '', 1).isdigit():
            expense_input = float(expense_input)
            data['expense'].append(expense_input)
            break
        else:
            print("Błąd: Kwota musi być liczbą.")


def update_total(data):
    data['total'] = sum(data['income']) - sum(data['expense'])
    
def show_total():
    print(f'{data["total"]:.2f}zł')

add_income()
add_expense()
update_total(data)
show_total()