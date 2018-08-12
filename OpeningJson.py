import json     #importujemy bibliotekę json - mamy możliwość operowania na plikach (.json)

plik = open("database.json").read()  # otwieramy plik json
                                     # można byłoby też otworzyć jako -- dane = json.loads([{"id": 1,"first_name": "Jeanette","last_name": "Penddreth",.....)
                                     #ale najpierw otwieramy plik i następnie wrzucamy dane do  json.loads - ułatwiamy pracę
dane = json.loads(plik)             # ładujemy jsona i zapisujemy go do dane
#print(dane) 						 #- podgląd naszego pliku json

print("Dane pierwszych dwóch osób")
print(dane[0])
print(dane[1])      #wyświetlają się nam wszystkie dane dwóch pierwszych osób

#przyjmijmy, że potrzebne będą nam tylko nazwiska i IP każdej osoby -tworzymy funkcję
print(type(dane))		        #sprawdzamy typy danych
print(type(dane[0]))
print(type(dane[0]["id"]))
for osoba in range(len(dane)):  #dlaczego nie zadziała nam "person in dane:"?
    nazwisko = dane[osoba]["last_name"]
    ip = dane[osoba]["ip_address"]
    print(f" Nazwisko: {nazwisko:10} IP: {ip}" )  #taki zapis umożliwia nam printowanie w kolummach--   nazwisko:n - gdzie n to odleglosc pomiedzy naziwskiem a IP