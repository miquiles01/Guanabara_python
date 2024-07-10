import random

numero_aleatorio = random.randint(0, 1000)

numero_jogador = int(input("Tente adivinhar o número (entre 0 e 1000): "))

if numero_jogador == numero_aleatorio:
    print("Parabéns! Você acertou o número!")
else:
    print(f"Que pena! Você errou. O número correto era {numero_aleatorio}.")
