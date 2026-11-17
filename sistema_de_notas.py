
print("CHEGOU O FIM DO ANO ESCOLAR E VAMOS VER SE VC FOI APROVADO OU NAO")

nota1 = float(input("ME DIGA SUA PRIMEIRA NOTA: "))
nota2 = float(input("AGORA SUA SEGUNDA NOTA: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("APROVADO")

elif media >= 5:
    print("RECUPERAÇÃO")

else:
    print("REPROVADO")
