# Pozyskujemy dane wejściowe - operację do wyliczenia
operacja = input("Wprowadź równanie do rozwiązania lub wpisz 'w' aby wyjść z programu: ")
# Wykorzystujemy pętlę nieskończoną do czasu wprowadzenia 'w', które przerywa działanie programu
while (operacja != "w"):
    # Wypisujemy rozwiązanie z wykorzystaniem funkcji eval() - proste!
    print("Rozwiązaniem Twojego równania [", operacja, "] jest:", eval(operacja))
    # Odpytujemy użytkownika o kolejny problem!
    operacja = input("Wprowadź kolejne równanie / problem do rozwiązania lub wpisz 'w' aby wyjść z programu: ")
    # Pętla trwa... aż wprowadzimy 'w'
