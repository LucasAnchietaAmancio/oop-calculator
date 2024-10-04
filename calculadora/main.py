from operacoes.divisao import divisao
from operacoes.soma import somar
from operacoes.subritacao import subitracao
from operacoes.multiplicacao import mult
from operacoes.avancados.cubo import cubo
from operacoes.avancados.quadrado import quadrado
import sys
class Calculadora:
    def __init__(self):
        self.x = 0
        self.y = 0

    
    def exponecia(self):
        exp = input("Deseja ralizar uma exponenciação ? (S/N) ").strip().upper()
        self.valida = False
        if  exp == 'S':
    
                quad_cub = input("Irá ser ao quadrado ? (tecle 1) Irá ser ao cubo ? (tecle 2) ")
                
                nmr = float(input("Digite o número para realizar a exponenciação: ").replace(",", "."))

                if quad_cub == '1':
                         
                         quadrado(nmr)

                elif quad_cub == '2':
                        
                        cubo(nmr)

                elif exp == 'N':
                        
                        pass
                
                else:
                     print("Digite uma informação válida")
        else:
            print("============================================================================================")
            pass
        
    def continuar(self):
            
            continua = input("Deseja continuar as operações ? (S/N)" ).strip().upper()
            if continua == 'S':
                    con = input("Deseja fazer outra exponenciação ? (S/N)" ).strip().upper()
                    if con == 'S':
                        self.exponecia()
                    elif con == 'N':
                        pass
                    else:
                        print("Digite uma informação válida")
            elif continua == 'N':
                    print("===================================================ENCERRANDO==============================================================")
                    sys.exit()       

    def getnum(self):
        while True:
            try:
                self.x = float(input("Digite o primeiro número: ").replace(",", "."))
                break  
            except: 
                print("Digite um número válido")
        
        while True:
            try:
                self.y = float(input("Digite o segundo número: ").replace(",", "."))
                break  
            except:
                print("Digite um número válido")

    def operador(self):
        operador = input("Digite o operador (+, -, /, *): ")
        if operador == '+':
            somar(self.x,self.y)
        elif operador == '-':
            subitracao(self.x,self.y)
        elif operador == '/':
            if self.y != 0:
                divisao(self.x,self.y)
            else:
                "Divisão por zero"
        elif operador == '*':
            mult(self.x,self.y)
        else:
            "Digite um operador válido"

if __name__ == '__main__':
    c = Calculadora()
    c.exponecia()
    c.continuar()
    c.getnum()
    c.operador()
    
     
