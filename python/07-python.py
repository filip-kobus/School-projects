def zlicz_a(tekst):
    liczba = 0
    for i in range(len(tekst)):
        if tekst[i] == "a":
            liczba += 1
    return liczba

wyraz = input("Podaj napis: ")
print("Liczba znakow a w twoim wyrazie to: ",zlicz_a(wyraz))