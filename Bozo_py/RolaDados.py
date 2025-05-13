import random
from Dado import Dado

class RolaDados:
    def __init__(self, n:int, seed:int):
        self.__dados=[]
        self.__r=random.Random(seed)


        for _ in range(n):
            self.__dados.append(Dado() if seed==0 else Dado(seed=self.__r.randint(1, 10000), lados=6))
    
    def rolar(self, rollDado:list[bool]):
        valores=[]
        for i in range(len(self.__dados)):
            if rollDado[i]:
                self.__dados[i].rolar()
                
            valores.append(self.__dados[i].getAtual())
                
        return valores


    def printDados(self):
        for i in range(5):
            base=i*8

            for dado in self.__dados:
                print(dado.stringDado()[base:base+7]+"    ", end="")
            print()
        print()