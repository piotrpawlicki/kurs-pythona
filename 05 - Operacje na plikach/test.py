import random
import openpyxl
from tkinter import Tk
from tkinter.filedialog import askopenfilename


#wczytanie pliku
Tk().withdraw()
file = askopenfilename(filetypes=[("Pliki excelowe", "*.xlsx")])

worksheets = openpyxl.load_workbook(file)
worksheets_names = worksheets.sheetnames

def enter_category(worksheets_names):
    print('Dostępne kategorie to :')
    for i, name in enumerate(worksheets_names):
        print(f'{i + 1} - {name}')
    while True:
        category = input('Wprowadź numer kategorii: ')
        try:
            category = int(category) - 1
            if category >= 0  and category < len(worksheets_names):
                break
        except TypeError:
            category = input('Błąd typu! Wprowadź numer kategorii: ')
    return category

def GUESS_WORDS():
    category = enter_category(worksheets_names)
    words_category = worksheets[worksheets_names[category]]
    collumn = 'A'
    start_row = 1
    row = start_row
    guess_list = []
    while True:
        guess_word = words_category[f'{collumn}{row}'].value
        if guess_word is None:
            break
        guess_list.append(guess_word)
        row += 1
    return guess_list


guess_list = GUESS_WORDS()
print(guess_list)
