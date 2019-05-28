def kalkulator():
    operacja = input('''
Podaj jaką operację chcesz wykonać:
+ dodawanie
- odejmowanie
* mnożenie
/ dzielenie
''')

    liczba1 = int(input('Podaj pierwszą liczbę: '))
    liczba2 = int(input('Podaj drugą liczbę: '))

    if operacja == '+':
        print('{} + {} = '.format(liczba1, liczba2))
        print(liczba1 + liczba2)

    elif operacja == '-':
        print('{} - {} = '.format(liczba1, liczba2))
        print(liczba1 - liczba2)

    elif operacja == '*':
        print('{} * {} = '.format(liczba1, liczba2))
        print(liczba1 * liczba2)

    elif operacja == '/':
        print('{} / {} = '.format(liczba1, liczba2))
        print(liczba1 / liczba2)

    else:
        print('Ooo Ty hakerze! Operacja nie jest jeszcze wspierana. Uruchom program raz jeszcze i wybierz poprawną operację :)')

    restart()

def restart():
    czyrestart = input('''
Czy chcesz coś jeszcze policzyć?
Wpisz T jeśli TAK lub N jeśli NIE :)
''')

    if czyrestart.upper() == 'T':
        kalkulator()
    elif czyrestart.upper() == 'N':
        print('Do zobaczenia!')
    else:
        restart()

kalkulator()