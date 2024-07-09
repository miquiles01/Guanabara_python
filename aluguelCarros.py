km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

preco_por_dia = 60.00
preco_por_km = 0.15
custo_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

print(f"O total a pagar é de R${custo_total:.2f}")
