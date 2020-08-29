import random
gen = random.randint(1, 101)
x=0
while True:
    x=x+1
    a = int(input("spejimas nuo 1 iki 100: "))
    if a == gen:
        print(f"Atspejai. Spejai: {x} kartus")
        input("uzbaikti?")
        break
    elif gen>a:
        print(f"{a} yra mazesnis uz spejama skaiciu")
    else:
        print(f"{a} yra didesnis uz spejama skaiciu")