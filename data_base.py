import sqlite3
sql = sqlite3.connect('db.sql', detect_types=1)
db = sql.cursor()

#query = 'CREATE TABLE telefony (id int, imie varchar, nazwisko varchar, numer int)'     # tworzy się tablica o nazwie "telefony" (nazwy wartości i ich typy)
query = 'DROP TABLE telefony'   #usuwanie tablicy
db.execute(query)   #wykonywanie 'query'

#dodajemy metodą INSERT INTO 'nazwa tablicy' (nazwy wartości) values ( odpowiednie dane do wprowadzenia)

query = "INSERT INTO telefony (id, imie, nazwisko, numer) values (1, 'Adam','Mackiewicz', 111111111)"
db.execute(query)
query = "INSERT INTO telefony (id, imie, nazwisko, numer) values (2, 'Daniel','Enterowy', 111111112)"
db.execute(query)
sql.commit()

# drukowanie tablicy 'telefony' * oznacza operację na wszystkich elementach
query = "SELECT * from telefony"
z = db.execute(query)
print(z.fetchall())