# Inicialização dos contadores
excelente = 0
bom = 0
ruim = 0

# Defina aqui a quantidade de entrevistados
quantidade = 50

# Estrutura de repetição FOR
for i in range(quantidade):
    print(f"\nEntrevistado {i+1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Avaliação do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opção: "))

    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

# Resultado final
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
