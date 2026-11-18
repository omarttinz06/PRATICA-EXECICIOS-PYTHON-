
print("BEM VINDO AO BRASIL ESCOLA")

usuario = input("DIGITE SEU USER: ")
senha = input("DIGITE SUA SENHA: ")

userv = "admin"
senhav = "2026"

confere1 = usuario == userv
confere2 = senha == senhav

if confere1 and confere2:
    print("ACESSO PERMITIDO")

elif confere1 and not confere2:
    print("SENHA INCORRETA")

elif confere2 and not confere1:
    print("USUARIO INCORRETO")

else:
    print("USUARIO E SENHA INCORRETOS")
