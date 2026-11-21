ano_de_nascimento = int(input("DIGITE SEU ANO DE NASCIMENTO: "))
ano_atual = int(input("DIGITE O ANO ATUAL: "))

if ano_de_nascimento >= ano_atual:
    print("ANO DE NASCIMENTO INVÁLIDO!")
else:
    idade = ano_atual - ano_de_nascimento
    print("Você tem aproximadamente", idade, "anos.")
