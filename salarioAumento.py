nomeFuncionario = str(input("Digite o nome do funcionário: "))
salarioAtual = float(input("Qual o salário atual do funcionário? R$"))
reajusteSalarial = salarioAtual * 0.15
novoSalario = salarioAtual + reajusteSalarial

print(f"O salário do funcionário {nomeFuncionario} é de R${salarioAtual:.2f}. Com o aumento de 15%, seu salário passará a ser R${novoSalario:.2f}.")
