tekst1 = input("Podaj pierwszy wyraz: ")
tekst2 = input("Podaj drugi wyraz: ")

def sprawdz(t1, t2):
    i = 0
    while i<len(t1) and i<len(t1) and t1[i] == t2[i]:
        i+= 1
    return i==len(t1) and i==len(t2)

if sprawdz(tekst1, tekst2) is True:
    print("Teksty sa identyczne!")
elif sprawdz(tekst1, tekst2) is False:
    print("Teksty sa rozne!")

input()