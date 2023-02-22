

'''53. Faça uma função que receba dois números inteiros a e b. Faça uma função que calcule e 
retorne a^b, sem utilizar funções prontas de potência'''


a = int(input('Digite o Número: '))
b = int(input('Digite a Potência: '))
print()

for c in range(a**b):

    print(f'{c+1}')

# ou o de baixo que só aparece o resultado

resultado = (a**b)
print(f"\nO resultado é: {resultado}\n")
