def transformator(wyraz, litera1, litera2):
  print("Wyraz po transformacji: {}".format(wyraz.replace(litera1, litera2)))

zmienna = input("Wprowadz wyraz: ")

transformator(zmienna, "a", "b")

input()
