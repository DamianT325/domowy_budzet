import csv
import os
# Main data including income, expense and total stored in dict
data = {'income': [], 'expense': [],'total': [] }
# Filename to save csv and also to check if already
filename = "dane.csv"
file_exist = os.path.isfile(filename)

def read_file(filename="dane.csv"):
    if file_exist:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)
            return list(csv_reader)
    else: 
        print("Brak pliku stwórz najpierw plik")

def update_file_total(filename="dane.csv", total=0):
    if file_exist:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)
            total_row = next(csv_reader)
            total_cell = total_row[2]
            total_cell = total

    else: 
        print("Brak pliku stwórz najpierw plik")


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
    if file_exist:
        data = read_file()
        update_file_total(2000)
        print(data[0][2])
    # data['total'].append(sum(data['income']) - sum(data['expense']))
  
        
    
def show_total():
    # print(f'{data["total"][0]:.2f}zł')
        if file_exist:
            total = read_file()
            print(f"Saldo (income-expsense): {total}")
        else: 
            print("Brak pliku stwórz najpierw plik")

def save_to_csv():
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        # check if file already exist and not adding headers
        if not file_exist:
            # Nagłowki 
            writer.writerow(['income', 'expense', 'total'])

        # for income, expense, total in zip(data['income'], data['expense'], data['total']):
        #     writer.writerow([income, expense, total])
        for i in range(len(data['income'])):
                writer.writerow([data['income'][i], data['expense'][i]])
    
    # print(f"Dane zostały poprawnie zapisane do pliku {filename}")

# TODO CSV handler dla write i read

# add_income()
# add_expense()
update_total(data)
# show_total()
# save_to_csv()
