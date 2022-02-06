def gwiazdki(x):
  for i in range(len(x)):
    if i+1 < len(x):
      print(x[i] + "*", end="")
    else:
      print(x[i], end="")

def poziom(x):
  for litera in x:
    print(litera, end="")

def pion(x):
  for litera in x:
    print(litera)

wyraz = input("Wprowadz wyraz: ")

print("\nWyraz w poziomie: ")

poziom(wyraz)

print("\n\nWyraz w pionie: \n", end = "")

pion(wyraz)

print("\nWyraz w poziomie odzielony gwiazdakami: ")

gwiazdki(wyraz)

input()