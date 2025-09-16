# ersezten

""" message = input('gib  satz: ')
print('dein Nachricht ist: ', message)
word1 = input('gib wort zu ersetzen: ')
word2 = input('gib wort zu ersetzen mit : ')
print(message.replace(word1, word2)) """


# List

""" kontiner = ['DE', 2, False, 'AR']
print(kontiner[0])
print(kontiner[1])
print(kontiner[2])
print(kontiner[3])
print(kontiner[-1])
print(kontiner[0:3])
print(kontiner)
print(kontiner[3][0])
print(type(kontiner))
print(type(kontiner[1]))
print(type(kontiner[2]))
print(type(kontiner[3]))


print(len(kontiner))

for i in kontiner:
    print(i) """


# List Methode

""" list1 = [1, 2, 3, 4, 5, 7]
list2 = ['banana', 'rot', 'rot', 'mango']

list1.append(6)     # fügen in ende von liste
print(list1)
list1.insert(0, 9)  # fügt in index 0 nummer 9
print(list1)
list1.extend(list2)  # mergt zwei listen
print(list1)
list1.remove(4)     # löscht elmente von Liste
print(list1)

print(list2.index('rot'))  # pint index von elment
print(list2.count('rot'))  # print wie viel kommt elment in linst

list3 = [2, 5, 1, 4, 7, 90, 5, 2]
list3.sort()
print(list3)
list3.reverse()
print(list3)

list3.clear()
print(list3)

list4 = [1, 2, 3, 4, 5]
list5 = list4.copy()
print(list5)

list5.pop()
print(list5)

list5.pop(2)
print(list5)

list5.remove(4)
print(list5)

del list5[2]
print(list5) """

# tuples

""" nummer = (1, 2, 3, 4)
print(nummer)
print(nummer[0])
print(nummer[1])
print(nummer[2])
print(nummer[3])
print(type(nummer))

for i in nummer:
    print(i)

print(len(nummer))

test = (1, 'test', True)
print(test)
print(type(test[2]))
 """

# Funktion

import asyncio
def hallo():
    print("Hallo Welt!")


hallo()


# ==================================
# 2. Funktion mit Parametern
# ==================================

def begruessung(name):
    print("Hallo", name)


begruessung("Max")


# ==================================
# 3. Funktion mit Rückgabewert
# ==================================
def quadrat(x):
    return x * x


print("Quadrat von 5:", quadrat(5))


# ==================================
# 4. Funktion mit mehreren Rückgaben (Tuple)
# ==================================
def rechnen(a, b):
    return a + b, a - b, a * b


ergebnis = rechnen(10, 5)
print("Mehrere Ergebnisse:", ergebnis)


# ==================================
# 5. Default-Parameter
# ==================================
def power(basis, exp=2):
    return basis ** exp  # ** = 3^3 basis hoch exp


print("Power(3):", power(3))        # hier nur basic
print("Power(3,3):", power(3, 3))  # hier basic und exp

# ==================================
# 6. Variable Argumente (*args)
# ==================================


def summe(*zahlen):
    return sum(zahlen)


"""" beliebig viele Argumente können übergeben werden. Diese Argumente werden in einem Tuple gespeichert"""

print("Summe:", summe(1, 2, 3, 4, 5))
print("Summe:", summe(1, 2, 3))

# ==================================
# 7. Keyword Argumente (**kwargs)
# ==================================


def info(**daten):
    for key, value in daten.items():
        print(key, ":", value)


"""   beliebig viele Keyword-Argumente können übergeben werden. """


info(name="Max", alter=25, stadt="Berlin")


# ==================================
# 8. Anonyme Funktion (Lambda)
# ==================================
def verdoppeln(x): return x * 2  # in ein Line


print("Lambda:", verdoppeln(7))


# ==================================
# 9. Funktion als Parameter (Higher-Order)
# ==================================
def anwenden(func, wert):
    return func(wert)


""" Hier wird anwenden eine höhere Funktion (higher-order function), weil sie eine andere Funktion (func) als Argument bekommt.
 lambda x: x + 10: bedeutet: definiere eine Funktion, die ein Argument x bekommt und als Ergebnis x + 10 zurückgibt“
            ( x+10,5)
 """
print("Higher Order:", anwenden(lambda x: x + 10, 5))


# ==================================
# 10. Funktion in Funktion (Nested Function)
# ==================================
def außen():
    def innen():
        return "Hallo aus innen()"
    return innen()


print(außen())

# Du kannst sogar eine Liste von Funktionen durchlaufen und anwenden auf jede loslassen:

funktionen = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x ** 2
]

wert = 4
for f in funktionen:
    print("Ergebnis:", anwenden(f, wert))


# ==================================
# 11. Closure (Funktion merkt sich Umgebung)
# ==================================
def multiplikator(faktor):
    print("faktor :", faktor)  # 3

    def mul(x):
        print("X :", x)  # 10
        print("faktor :", faktor)
        return x * faktor

    return mul


mal3 = multiplikator(3)
print("Closure:", mal3(10))


# ==================================
# 12. Rekursive Funktion
# ==================================
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n-1)


print("Fakultät von 5:", fakultaet(5))


# ==================================
# 13. Generator (yield)
# ==================================
def generator():
    for i in range(3):
        yield i


print("Generator Beispiel:")
for val in generator():
    print(val)


# ==================================
# 13. Generator (yield) mit Liste
# ==================================#
def liste():
    return [0, 1, 2]


for val in liste():
    print(val)

# ==================================
# 14. Decorator (Funktion verändert Funktion)
# ==================================


def dekorator(func):
    def wrapper():
        print("Vor der Funktion")
        func()
        print("Nach der Funktion")
    return wrapper


@dekorator
def sag_hallo():
    print("Hallo!")


sag_hallo()


# ==================================
# 15. Asynchrone Funktion (async / await)
# ==================================


async def async_funktion():
    print("Async Start")
    await asyncio.sleep(1)
    print("Async Ende")

asyncio.run(async_funktion())  # Nur aktivieren wenn async getestet werden soll

# ---------------------------------------------------------------------------------------------------------------

# ------------------------------------
# Bedingungen (if / elif / else)
# ------------------------------------

zahl = 10
# zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print(zahl, "Die Zahl ist positiv")
elif zahl == 0:
    print("Die Zahl ist null")
else:
    print("Die Zahl ist negativ")

# Vergleichsoperatoren
a, b = 5, 3
print("a == b:", a == b)    # Gleich
print("a != b:", a != b)    # Ungleich
print("a > b:", a > b)      # Größer
print("a < b:", a < b)      # Kleiner
print("a >= b:", a >= b)    # Größer oder gleich
print("a <= b:", a <= b)    # Kleiner oder gleich")

# Logische Operatoren
x, y = True, False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\n=== FOR-SCHLEIFEN ===")

# 1. For mit range
print("Zahlen 0 bis 4:")
for i in range(5):
    print(i)

# 2. For mit Start, Ende, Schritt
print("Zahlen 10 bis 0 (Schritt -2):")
for i in range(10, -1, -2):
    print(i)

# 3. For über Liste
farben = ["rot", "grün", "blau"]
print("Liste durchlaufen:")
for f in farben:
    print(f)

# 4. For über Dict
person = {"name": "Max", "alter": 25}
print("Dictionary durchlaufen (Keys & Values):")
for key, value in person.items():
    print(key, ":", value)

# 5. For über Set
zahlen_set = {1, 2, 3}
print("Set durchlaufen:")
for z in zahlen_set:
    print(z)

# 6. For über String
wort = "Python"
print("Buchstaben im String:")
for buchstabe in wort:
    print(buchstabe)

print("\n=== WHILE-SCHLEIFE ===")

n = 5
while n > 0:
    print("Countdown:", n)
    n -= 1

print("Fertig!")

print("\n=== BREAK / CONTINUE / ELSE ===")

# Break: Schleife abbrechen
for i in range(10):
    if i == 3:
        print("Stop bei", i)
        break
    print(i)

# Continue: Iteration überspringen
for i in range(5):
    if i == 2:
        continue
    print("Zahl:", i)

# For mit else (läuft, wenn Schleife NICHT mit break abgebrochen wird)
for i in range(3):
    print("Durchlauf:", i)
else:
    print("Schleife ohne break beendet!")

# While mit else
k = 0
while k < 3:
    print("While Schritt:", k)
    k += 1
else:
    print("While normal beendet")


# 0 bis 11
for i in range(12):
    print(i)

# 1 bis 11
for i in range(1, 12):
    print(i)

# Nur gerade Zahlen von 0 bis 10
for i in range(0, 12, 2):
    print(i)

# Rechner
""" while True:
    q1 = int(input("Gib eine Zahl ein: "))

    q2 = int(input("Gib eine Zahl ein: "))

    g = q1+q2
    print(g) """


# try und exception
try:
    zahl = 10
    teiler = 0
    ergebnis = zahl / teiler   # das wirft ZeroDivisionError
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("Fehler: Division durch 0 ist nicht erlaubt!")

print("Programm läuft weiter...")

try:
    text = "abc"
    zahl = int(text)   # wirft ValueError
    print("Zahl:", zahl)

except ValueError:
    print("Fehler: Umwandlung in int fehlgeschlagen!")
except TypeError:
    print("Fehler: Falscher Typ verwendet!")


try:
    f = open("test.txt", "r")
    inhalt = f.read()
    print(inhalt)

except FileNotFoundError:
    print("Fehler: Datei nicht gefunden!")
finally:
    print("Dieser Block wird immer ausgeführt (z. B. zum Aufräumen).")


# lesen file

try:
    f = open("text.txt", "r")
    inhalt = f.read()
    print("lesen: ", inhalt)
    # print("Test1 :", f.readlines()[0])
    f.close()

except FileNotFoundError:
    print("Fehler: Datei nicht gefunden!")
finally:
    print("Dieser Block wird immer ausgeführt (z. B. zum Aufräumen).")

# schreiben file

try:
    f = open("text.txt", "w")
    f.write("test neu von pc")

    f = open("text.txt", "r")
    inhalt = f.read()
    print("schreiben", inhalt)

    f.close()

except FileNotFoundError:
    print("Fehler: Datei nicht gefunden!")
finally:
    print("Dieser Block wird immer ausgeführt (z. B. zum Aufräumen).")


# classes und objekten

class Person1:
    def __init__(self, name1, alter1):  # konstrakutr
        self.name = name1
        self.alter = alter1

    def begruessung(self):
        print("Hallo", self.name)

    def info(self):
        print("Name:", self.name)
        print("Alter:", self.alter)

    def alter_aendern(self, neuer_alter):
        self.alter = neuer_alter


person1 = Person1("Max", 25)
person1.begruessung()
person1.info()
person1.alter_aendern(30)
person1.info()


# inheritance
class Student():
    name = 'tim'
    age = 20


# python shell
