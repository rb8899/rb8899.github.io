import turtle
import pickle

def konwertuj_nr_na_kolor(kod_koloru):
    kody = ["black", "red", "blue", "green", "pink", "orange", "violet"]
    return kody[kod_koloru]

def ksztalt(zolw, ilosc, dlugosc, kolor=0, grubosc=2):
    zolw.color(konwertuj_nr_na_kolor(kolor))
    zolw.width(grubosc)
    for i in range(0,ilosc):
        zolw.right(360/ilosc)
        zolw.forward(dlugosc)


# poczatek programu
bob = turtle.Turtle()
glowne_okno = turtle.Screen()
glowne_okno.setup(1000, 800)
glowne_okno.delay(2)

bob.speed(0)
print("Czy chcesz importować dane?")
if input() == "tak":
    data_imported = True
    print("Z jakiego pliku chcesz importować?")
    input_file_import = open(input()+'.dat', 'rb')
    input_file_data = pickle.load(input_file_import)
    input_file_import.close()
    dlugosc_boku = input_file_data["dlugosc_boku"]
    ilosc_bokow = input_file_data["ilosc_bokow"]
    grubosc = input_file_data["grubosc"]
    kolor = input_file_data["kolor"]
    print("Wciśnij ENTER aby rysować")
    input()
else:
    data_imported = False
    dlugosc_boku = int(turtle.numinput("Wpisz dane","Wpisz długość boku"))
    ilosc_bokow = int(turtle.numinput("Wpisz dane","Wpisz ilość boków"))
    grubosc = int(turtle.numinput("Wpisz dane","Wpisz grubość pisma"))
    kolor = int(turtle.numinput("Wpisz dane","Wpisz kod koloru pisma:\n0: czarny\n1: czerwony\n2: niebieski\n3: zielony\n4: różowy\n5: pomarańczowy\n6: fioletowy"))

data = {
    "dlugosc_boku": dlugosc_boku,
    "ilosc_bokow": ilosc_bokow,
    "grubosc": grubosc,
    "kolor": kolor
}

ksztalt(bob, ilosc_bokow, dlugosc_boku, kolor, grubosc)
if data_imported != True:
    print("Czy zapisać dane?")
    if input() == "tak":
        print("Jak się ma nazwywać plik?")
        data_file = open(input()+".dat", 'wb')
        pickle.dump(data, data_file)
        data_file.close()
print("Wciśnij ENTER by zakończyć")
input()
exit()
turtle.mainloop()   # czekaj w petli glownej na zakonczenie aplikacji
