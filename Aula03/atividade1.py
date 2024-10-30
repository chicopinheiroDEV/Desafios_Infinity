import random

while True:
    choise = input("Deseja fazer a escolha de uma idade? (S/N) -> ")
    if choise.upper() == "N":
        break
    elif choise.upper() == "S":
        # age = random.randint(0,100)
        age = int(input("Informe a sua idade: "))
        if age < 12:
            print(f"Sua idade é {age}, portanto você é uma Criança")
        elif age <= 17:
            print(f"Sua idade é {age}, portanto você é um Adolescente")
        elif age <= 59:
            print(f"Sua idade é {age}, portanto você é um Adulto")
        elif age >= 60:
            print(f"Sua idade é {age}, portanto você é um Idoso")
    