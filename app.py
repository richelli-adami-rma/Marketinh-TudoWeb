# Inicialização dos contadores
excelente = 0
ruim = 0

# Loop para 50 entrevistados
for i in range(1, 51):
    print(f"\nEntrevistado {i}")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Avaliação do atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    opiniao = int(input("Digite sua opinião (1, 2 ou 3): "))
    
    # Estrutura de decisão
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
    elif opiniao == 2:
        pass  # Não precisamos contar "BOM" neste caso
    else:
        print("Opção inválida!")

# Resultado final
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
