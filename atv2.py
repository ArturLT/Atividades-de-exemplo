def fatorial(num):
    if num < 0:
        return "Não existe fatorial para números negativos"

    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result


num = int(input('Digite um número: '))

while num < 1:
    print("Número inválido. Digite um número inteiro positivo.")
    num = int(input('Digite um número: '))

result = fatorial(num)
print(f'O fatorial de {num} é {result}')
