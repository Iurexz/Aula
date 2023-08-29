"""""
print("Escolha uma opção:")
print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
opcao = int(input("Opção"))

if opcao == 1:
    print("ggg") #código para opção 1
elif opcao == 2:
    print("jjjj") #código para opção 2
elif opcao == 3:
    print("sair") #código para opção 3
else:
    print ("Opção inválida.")
"""

"""""
opcao=int
while opcao !=3:
      print("Escolha uma opção: ")
      print("1 - Adicionar um novo item")
      print("2 - Ver todos os itens")
      print("3 - Sair")  
      opcao = int(input("Opção escolhida: "))

if opcao == 1:
      print("ffff")
elif opcao == 2:
        print("jaj")
elif opcao == 3:
        print("Encerrando o aplicativo...")
else:
        print("Opção inválida.")
"""

""""""

"""""""""
list = ['viado','gay','omen','ain']
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[-2])
"""

"""""
list = [10, 50, 30, 40, 25, 60, 5]
print(list[0:7])
print(list[1:7])
print(list[1:])
print(list[::7])
"""

"""""
dados = ['Iure Costa da Silva', 19, 1.74, True]
print ("Nome:.......:", dados[0])
print ("Idade.......:", dados[1])
print ("Estatura:...:", dados[2])
print ("Usa a rede social Discord?")

if dados[3] == True:
    print("Usa Discord.: Sim")
else:
    print("Usa Discord.: Não")
"""
"""""
list=[10,50,30,40,25,60,5]
print('Antes do apprend:', list)
list.append(3)
print('depois do apprend:', list)
"""
""""
list = [1, 3, 12, 8, 2]
list.insert(2,10)
print('depois do insert:',list)
"""
"""""
atrizes = ["Paolla de Oliveira"]
atrizes.append("Sheron Menezes")
atrizes.insert(1,"Raquel Nunes")
print (atrizes)
"""

list = ['fruta','prato','teclado','viado']
for fruta in list:
    print(list)
