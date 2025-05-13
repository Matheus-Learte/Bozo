class Placar:
    def __init__(self):
        self.__placar = []
        self.__taken = []
        
        for i in range(10):
            self.__taken.append(False)
            self.__placar.append(0)

    def add(self, posicao:int, dados:list[int]):
        if self.__taken[posicao-1]:
            raise ValueError("Posição ocupada")
        k=0

        match(posicao):
            case 1:
                k = self.__contador(1, dados)
            case 2:
                k = 2*self.__contador(2, dados)
            case 3:
                k = 3*self.__contador(3, dados)
            case 4:
                k = 4*self.__contador(4, dados)
            case 5:
                k = 5*self.__contador(5, dados)
            case 6:
                k = 6*self.__contador(6, dados)
            case 7:
                if self.__verificaFull(dados):
                    k=15
            case 8:
                if self.__verificaSeqMaior(dados):
                    k = 20
            case 9:
                if self.__verificaQuadra(dados):
                    k = 30
            case 10:
                if self.__verificaQuina(dados):
                    k = 40
            case _:
                raise ValueError("Posição Ilegal")
        
        self.__placar[posicao-1]=k
        self.__taken[posicao-1]=True

    def __contador(self, numero:int, dados:list[int]):
        cont=0

        for k in dados:
            if k==numero:
                cont+=1
        
        return cont
    
    def getScore(self):
        cont=0

        for i in range(10):
            cont+=self.__placar[i]
        
        return cont
    
    def __verificaFull(self, dados:list):
        aux = dados.copy()
        aux.sort()

        return (aux[0]==aux[1] and aux[1]==aux[2] and aux[3]==aux[4]) or (aux[0]==aux[1] and aux[2]==aux[3] and aux[3]==aux[4])

    def __verificaQuadra(self, dados:list):
        aux = dados.copy()
        aux.sort()

        return (aux[0]==aux[1] and aux[1]==aux[2] and aux[2]==aux[3]) or (aux[1]==aux[2] and aux[2]==aux[3] and aux[3]==aux[4])

    def __verificaQuina(self, dados:list):
        return dados[0]==dados[1] and dados[1]==dados[2] and dados[2]==dados[3] and dados[3]==dados[4]

    def __verificaSeqMaior(self, dados:list):
        aux = dados.copy()
        aux.sort()

        return aux[0]==aux[1]-1 and aux[1]==aux[2]-1 and aux[2]==aux[3]-1 and aux[3]==aux[4]-1

    def printPlacar(self):
        for i in range(3):
            print(("{:^4}".format(self.__placar[i]) if self.__taken[i] else "("+str(i+1)+") ")+"   |   ", end="")
            print(("{:^4}".format(self.__placar[i+6]) if self.__taken[i+6] else "("+str(i+7)+") ")+"   |  ", end="")
            print("{:^4}".format(self.__placar[i+3]) if self.__taken[i+3] else "("+str(i+4)+") ")
            print("-------|----------|-------")
        
        print("       |   "+("{:^4}".format(self.__placar[9]) if self.__taken[9] else "("+str(10)+")")+ "   |")
        print("       +----------+\n")
