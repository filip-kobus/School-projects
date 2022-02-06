wyraz = input("Podaj wyraz: ")

def zamiana(wyraz):
    nowy = [letter for letter in wyraz]
    nowy[0] = wyraz[-1]
    nowy[-1] = wyraz[0]
    return "".join(nowy)
    
print(f'Wyraz po zamianie: {zamiana(wyraz)}')