import math

angulo_graus = float(input("Digite um ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"O seno de {angulo_graus} graus é: {seno}")
print(f"O cosseno de {angulo_graus} graus é: {cosseno}")
print(f"A tangente de {angulo_graus} graus é: {tangente}")
