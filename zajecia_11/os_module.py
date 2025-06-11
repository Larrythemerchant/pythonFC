import os

print(os.getcwd())
print(os.listdir())
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())

nazwa_pliku = input("nazwa pliku: ")
if os.path.exists(nazwa_pliku):
    print("plik istnieje")

print(os.path.join(os.getcwd(), nazwa_pliku))
