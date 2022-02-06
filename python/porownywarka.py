podkresl = chr(8254)  #pobieram znak górnego myślnika, który będzie służył za podkreślenie

def porownywarka(w1, w2):
    pomoc1 = w1.split(" ") #każdy z wyrazów tekstu zapisuję w listach pomoc1 i pomoc2
    pomoc2 = w2.split(" ")
    bledy = ""   #string który będzie zawierał myślniki podkreślające różnice w tekście
    
    if len(pomoc1) != len(pomoc2):  #jeżeli teksty będą zawierać różną ilość wyrazó program zakończy działanie
        return "Teksty musza miec taka sama liczbe wyrazow!!!"

    for i in range(len(pomoc1)):
      lista = znajdz_bledy(pomoc1[i], pomoc2[i])
      bledy += wypisz_bledy(lista, len(pomoc1[i]), len(pomoc2[i])) #różnice każdego wyrazu dodawane są do różńic całeg tekstu
      
    return bledy
    
def znajdz_bledy(w1, w2):
  lista = []
  for i in range(min(len(w1),len(w2))):
    if w1[i] != w2[i]:
      lista.append(i)   #zapisuję indeksy znaków które się różnią
  return lista

def wypisz_bledy(lista, l1, l2):
  bledy = ""
  if l1 < l2 or l1 > l2:    #kiedy wyrazy mają różne długości cały wyraz zostaje podkreślony
    for i in range(l2):
      bledy += podkresl
    return bledy + " "

  for i in range(l1):
    if i in lista:    
      bledy += podkresl
      continue
    bledy += " "
  return bledy + " "

def main():
  print(
    "Witaj w programie porownującym dwa teksty.\nPorownywane teksty powinny zawierac ta sama liczbe wyrazow, w innym wypadku program nie zadziala!!!\n"
    )
  
  tekst1 = input("Podaj pierwszy tekst: ")
  tekst2 = input("Podaj drugi tekst: ")

  print(f'\nTekst pierwszy: \n{tekst1}')
  print(f'Tekst drugi: \n{tekst2}')
  print(porownywarka(tekst1, tekst2))

if __name__ == "__main__":  #jeżeli skrypt zostanie uruchominy poprzez wywołanie jego imienia to wykona się funkcja main()
  main()
  input()