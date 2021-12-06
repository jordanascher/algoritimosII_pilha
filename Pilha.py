from No import No

class Pilha:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None 
        self.tamanho = 0

    def adicionar(self, valor):
        self.tamanho += 1

        no = No(valor)

        if(self.tamanho == 1):
            self.primeiro = no 
        elif(self.tamanho > 1):
            self.ultimo.proximo = no

        self.ultimo = no

    def remover(self):
        self.tamanho -= 1

        if(self.tamanho == 1):
            self.primeiro.proximo = None
            self.ultimo = self.primeiro
        elif (self.tamanho > 1):

            aux = self.primeiro
            
            while(aux):
                if(aux.proximo):
                    if(aux.proximo == self.ultimo):
                        # print('penultimo é :'+str(aux.valor))
                        aux.proximo = None
                        self.ultimo = aux

                aux = aux.proximo

    def imprimir(self):
        txt = ""

        if self.tamanho == 0:
            txt = "Pilha vazia"
        else:
            aux = self.primeiro
            
            while(aux):
                txt = txt + str(aux.valor) + " - "
                aux = aux.proximo               
        
        print(txt)
        print("-----------------------------")


