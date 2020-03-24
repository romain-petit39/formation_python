a = 52
b = 'toto'
c = input("Test avec une division, fait plusieurs tests ")
annee = input("entrer une année ")

try:
    annee = int(annee)
except:
    print("il faut mettre une annee stp")


try:
    c = int(c)
    result = a / b
except TypeError:
    print("il doit y avoir un string")

try:
    result = a / c
except ZeroDivisionError:
    print("tu ne peux pas diviser par zero")
except TypeError:
    print("il doit y avoir un string")
finally:
    print("fin du try")