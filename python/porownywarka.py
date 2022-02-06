podkresl = chr(8254)  #pobieram znak górnego myślnika, który będzie służył za podkreślenie

class porownywarka:
  def __init__(self):
    self.bledy = ""   #string który będzie zawierał myślniki podkreślające różnice w tekście
    
    print(
      "Witaj w programie porownującym dwa teksty.\nPorownywane teksty powinny zawierac ta sama liczbe wyrazow, w innym wypadku program nie zadziala!!!\n"
      )
    
    self.w1 = input("Podaj pierwszy tekst: ")
    self.w2 = input("Podaj drugi tekst: ")

    print(f'\nTekst pierwszy: \n{self.w1}')
    print(f'Tekst drugi: \n{self.w2}')
    print(self.porownywarka())
  
  def porownywarka(self):
      pomoc1 = self.w1.split(" ") #każdy z wyrazów tekstu zapisuję w listach pomoc1 i pomoc2
      pomoc2 = self.w2.split(" ")  
      
      if len(pomoc1) != len(pomoc2):  #jeżeli teksty będą zawierać różną ilość wyrazó program zakończy działanie
          return "Teksty musza miec taka sama liczbe wyrazow!!!"

      for i in range(len(pomoc1)):
        lista = self.znajdz_bledy(pomoc1[i], pomoc2[i])
        self.bledy += self.wypisz_bledy(lista, len(pomoc1[i]), len(pomoc2[i])) #różnice każdego wyrazu dodawane są do różńic całeg tekstu
        
      return self.bledy
      
  @staticmethod
  def znajdz_bledy(w1, w2):
    lista = []
    for i in range(min(len(w1),len(w2))):
      if w1[i] != w2[i]:
        lista.append(i)   #zapisuję indeksy znaków które się różnią
    return lista

  @staticmethod
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
    

if __name__ == "__main__":  #jeżeli skrypt zostanie uruchominy poprzez wywołanie jego imienia to wykona się funkcja main()
  porownywarka()
  input()
