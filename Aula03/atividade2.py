import math

list_number = []

for _ in range (3):
    number = float(input("Informe o número que deseja adicionar a lista: "))
    list_number.append(number)

max_number = max(list_number)
min_number = min(list_number)  
print(f"O maior número é {max_number} e o menor número é {min_number}")