# kKurs von elzero

""" -einfache zu schreiben und sauber und Fehler behandlung ,OPP Debugging
- web ENtwicklung, (Django, Flask)
-Games
- Desktop Apps
 -HAcking
 -Machine Lerning
 -AI& Robots
 Automation
 web Scrapping  (python ist expert in diese Bereich) 
 android games """


# Ganze Zahl (Integer)
import asyncio
zahl = 42
print("Integer:", zahl, type(zahl))

# Fließkommazahl (Float)
kommazahl = 3.14
print("Float:", kommazahl, type(kommazahl))

# Komplexe Zahl (Complex)
komplex = 2 + 3j
print("Complex:", komplex, type(komplex))

# Zeichenkette (String)
text = "Hallo Welt"
print("String:", text, type(text))

# Wahrheitswert (Boolean)
wahrheit = True
print("Boolean:", wahrheit, type(wahrheit))

# Liste (List)
meine_liste = [1, 2, 3, "Apfel"]
print("Liste:", meine_liste, type(meine_liste))

# Tupel (Tuple) gleich wie List
mein_tupel = (10, 20, 30)
print("Tuple:", mein_tupel, type(mein_tupel))

# Menge (Set)
mein_set = {1, 2, 3, 3}
print("Set:", mein_set, type(mein_set))

# Frozenset (unveränderliche Menge)
mein_frozenset = frozenset([1, 2, 2, 3])
print("Frozenset:", mein_frozenset, type(mein_frozenset))

# Wörterbuch (Dictionary) wie enum aber jeder teil hat wert
mein_dict = {"name": "Max", "alter": 25}
print("Dictionary:", mein_dict, type(mein_dict))

# Bytes
meine_bytes = b"Hallo"
print("Bytes:", meine_bytes, type(meine_bytes))

# Bytearray (veränderbar)
mein_bytearray = bytearray([65, 66, 67])
print("Bytearray:", mein_bytearray, type(mein_bytearray))

# Memoryview (Speicheransicht)
mein_memory = memoryview(b"Python")
print("Memoryview:", mein_memory, type(mein_memory))

# None (Kein Wert)
nichts = None
print("None:", nichts, type(nichts))


# -----------------------------------------------------------------------
# ---------------------------
# Python Datentypen Beispiele
# ---------------------------

# Globale Variablen
global_text = "Globale Variable"
global_zahl = 100

print("=== Globale Variablen ===")
print(global_text, type(global_text))
print(global_zahl, type(global_zahl))
print()

# Eingabe und Ausgabe
name = input("Gib deinen Namen ein: ")
alter = int(input("Gib dein Alter ein (Zahl): "))

print("\nHallo,", name, "du bist", alter, "Jahre alt.")
print("Typ von name:", type(name))
print("Typ von alter:", type(alter))
print()

# ---------------------------
# Operationen mit Datentypen
# ---------------------------

print("=== Zahlen (int, float, complex) ===")
a = 10
b = 3
c = 2.5
z = 2 + 3j

print("Addition:", a + b)
print("Subtraktion:", a - b)
print("Multiplikation:", a * b)
print("Division:", a / b)
print("Ganzzahl-Division:", a // b)
print("Modulo:", a % b)
print("Potenz:", a ** b)
print("Float-Operation:", c * 2)
print("Komplexe Zahl:", z * (1 + 2j))
print()

print("=== Strings ===")
text = "Python"
print("Verkettung:", text + " Rocks")
print("Wiederholung:", text * 3)
print("Index:", text[0])
print("Slice:", text[1:4])
print("Groß:", text.upper())
print("Klein:", text.lower())
print("Länge:", len(text))
print()

print("=== Listen ===")
meine_liste = [1, 2, 3, "Apfel"]
print("Original:", meine_liste)
meine_liste.append("Banane")  # einfügen
print("Append:", meine_liste)
meine_liste.remove(2)
print("Remove:", meine_liste)
meine_liste[0] = 99
print("Änderung:", meine_liste)
print("Slice:", meine_liste[1:3])
print()

print("=== Tupel ===")
mein_tupel = (10, 20, 30)
print("Zugriff:", mein_tupel[1])
print("Länge:", len(mein_tupel))
print()

print("=== Mengen (Set) ===")
mein_set = {1, 2, 3}
anderes_set = {3, 4, 5}
print("Union:", mein_set | anderes_set)
print("Intersection:", mein_set & anderes_set)
print("Difference:", mein_set - anderes_set)
print()

print("=== Dictionary ===")
mein_dict = {"name": "Max", "alter": 25}
print("Zugriff:", mein_dict["name"])
mein_dict["stadt"] = "Berlin"
print("Hinzufügen:", mein_dict)
print("Keys:", mein_dict.keys())
print("Values:", mein_dict.values())
print()

print("=== Bool ===")
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)
print()

print("=== Bytes, Bytearray ===")
meine_bytes = b"ABC"
print("Bytes:", meine_bytes)
mein_bytearray = bytearray([65, 66, 67])
mein_bytearray[0] = 90
print("Bytearray:", mein_bytearray)
print()

print("=== None ===")
nichts = None
print("None Beispiel:", nichts, type(nichts))

# ---------------------------------------------------------

# ------------------------------------
# Bedingungen (if / elif / else)
# ------------------------------------
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist positiv")
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


# --------------------------------------------------------------------------------------------------

# ==================================
# 1. Normale Funktion (def)
# ==================================
def hallo():
    print("Hallo Welt!")


hallo()


# ==================================
# 2. Funktion mit Parametern
# ==================================
print("------------ Funktionen -------------------wd")


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
    return basis ** exp   # 3^3 basis hoch exp


print("Power(3):", power(3))
print("Power(3,3):", power(3, 3))


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

# beliebig viele Keyword-Argumente können übergeben werden.


info(name="Max", alter=25, stadt="Berlin")


# ==================================
# 8. Anonyme Funktion (Lambda)
# ==================================
def verdoppeln(x): return x * 2


print("Lambda:", verdoppeln(7))


# ==================================
# 9. Funktion als Parameter (Higher-Order)
# ==================================
def anwenden(func, wert):
    return func(wert)

# Hier wird anwenden eine höhere Funktion (higher-order function), weil sie eine andere Funktion (func) als Argument bekommt.


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
