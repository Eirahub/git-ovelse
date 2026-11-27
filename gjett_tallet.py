import random

igjen = "j"
poeng = 0
while igjen == "j":
    tall = random.randint(1, 10)
    while True:
        gjett = int(input("Gjett et tall fra 1 til 10: "))
        if gjett == tall:
            print("Riktig!")
            poeng += 1
            break
        print("Feil, prøv igjen")
    print("Poeng:", poeng)
    igjen = input("Vil du spille igjen? (j/n) ")
