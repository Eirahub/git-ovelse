import random

igjen = "j"
while igjen == "j":
    tall = random.randint(1, 10)
    while True:
        gjett = int(input("Gjett et tall fra 1 til 10: "))
        if gjett == tall:
            print("Riktig!")
            break
        print("Feil, prøv igjen")
    igjen = input("Vil du spille igjen? (j/n) ")
