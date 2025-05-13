from Placar import Placar
from RolaDados import RolaDados

seed = int(input("Digite a semente (zero para aleatório): "))
dados = RolaDados(seed=seed, n=5)
placar = Placar()

placar.printPlacar()

for round in range(10):
    print("****** Rodada " + str(round+1))
    input("Pressione ENTER para lançar os dados\n")

    aux=[]
    for _ in range(5):
        aux.append(True)
    
    dados.rolar(aux)
    print("1          2          3          4          5")
    dados.printDados()

    aux=[not x for x in aux]
    read=input("Digite os números dos dados que quiser TROCAR. Separados por espaços.\n")
    auxiliar=read.split()
    for posicao in auxiliar:
        if posicao.isdigit():
            temp = int(posicao)
            
            if temp<6:
                aux[temp-1]=True
    dados.rolar(aux)
    print("1          2          3          4          5")
    dados.printDados()

    aux=[False for x in aux]
    read=input("Digite os números dos dados que quiser TROCAR. Separados por espaços.\n")
    auxiliar=read.split()
    for posicao in auxiliar:
        if posicao.isdigit():
            temp = int(posicao)
            
            if temp<6:
                aux[temp-1]=True
    values=dados.rolar(aux)
    print("1          2          3          4          5")
    dados.printDados()

    pos=0
    while(pos<=0):
        try:
            pos=int(input("Escolha a posição que quer ocupar com essa jogada ===> "))

            if pos>10 or pos<=0:
                pos=0
            else:
                placar.add(pos, values)
        except ValueError:
            pos=0

        if pos==0:
            print("Valor inválido. Posição ocupada ou inexistente.")
    
    print("\n\n")
    placar.printPlacar()

print("***********************************")
print("***")
print("*** Seu escore final foi: {:d}".format(placar.getScore()))
print("***")
print("***********************************")