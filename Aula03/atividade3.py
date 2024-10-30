numbers = []
pair_numbers = []
odd_numbers = []

for i in range (1, 11):
    number = int(input(f"Informe o {i}° número inteiro: "))
    if number % 2 == 0:
        pair_numbers.append(number)
    else: 
        odd_numbers.append(number)
        
print(f"A quantidade de números pares são {len(pair_numbers)}")
print(f"A quantidade de números ímpares são {len(odd_numbers)}")