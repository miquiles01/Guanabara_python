preco_original = float(input("Digite o preço do produto: R$ "))

desconto = preco_original * 0.05

preco_com_desconto = preco_original - desconto

print(f"O preço original do produto é: R$ {preco_original:.2f}")
print(f"O valor do desconto é: R$ {desconto:.2f}")
print(f"O novo preço do produto com 5% de desconto é: R$ {preco_com_desconto:.2f}")
