print('test Python')
print("*" * 10)

nummer1 = 10
nummer2 = 20

name = "Yassin"

print(nummer1)
print(name)

print(type(nummer1))
print(type(name))

# >format dokument  um die Code klar schreiben oder bei Sitting formatOnsave
x = 5

# strg + r um file zu run

#  Jython ist java code in Python Programm
#  Cpython ist c code in Python Programm

# Kurs von Youtube :https://www.youtube.com/watch?v=K5KVEU3aaeQ    , Zeit: 31:48


message = """t
Hi das ist voll Text  in ein String

r"""

print(message)

print(len(message))

print(message[0])
print(message[-1])
print("Test\n" + message[0:5])

print(bool(None))

if nummer1 > nummer2:
    print("nummer1 > nummer2")
else:
    print("nummer1 < nummer2")

Text = "richtig " if nummer1 > 23 else "nicht richtig"

print(Text)

# Operation

print(nummer1 + nummer2)
print(nummer1 - nummer2)
print(nummer1 * nummer2)
print(nummer1 / nummer2)
print(nummer1 // nummer2)

# Operation and or

print(nummer1 & nummer2)
print(nummer1 | nummer2)
print(nummer1 ^ nummer2)


Max = True
Min = False

if Max and Min:
    print("Max and Min")
else:
    print("Max or Min")

if Max or Min:
    print("Max or Min")
else:
    print("Max and Min")
