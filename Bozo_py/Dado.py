import random

class Dado:
    def __init__(self, seed:int = 0, lados:int = 6):
        self.__lados=lados
        self.__atual=0

        if seed!=0:
           self.__r=random.Random(seed)
        else:
            self.__r=random.Random()
        
        self.rolar()
    
    def rolar(self):
        self.__atual=self.__r.randint(1, self.__lados)
        return self.__atual

    def getAtual(self):
        return self.__atual
    
    def stringDado(self):
        s010="|  *  |"
        s100="|*    |"
        s001="|    *|"
        s000="|     |"
        s101="|*   *|"
        s111="|* * *|"

        if self.__lados!=6:
            print("Não tem representação para o dado")
        else:
            s="+-----+\n"

            match(self.getAtual()):
                case 1:
                    s+=s000+"\n"+s010+"\n"+s000+"\n"
                case 2:
                    s+=s100+"\n"+s000+"\n"+s001+"\n"
                case 3:
                    s+=s100+"\n"+s010+"\n"+s001+"\n"
                case 4:
                    s+=s101+"\n"+s000+"\n"+s101+"\n"
                case 5:
                    s+=s101+"\n"+s010+"\n"+s101+"\n"
                case 6:
                    s+=s111+"\n"+s000+"\n"+s111+"\n"

            s+="+-----+\n"
        
        return s