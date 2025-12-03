from utilitarios import validar_entrada
def menu_operadores() ->  None:

    print("Operadores disponíveis: ")
    print("+ -> SOMA")
    print("- -> SUBTRAÇÃO")
    print("*  -> MULTIPLICAÇÃO")
    print("/  -> DIVISÃO")

def ler_operador() -> str:

    lista = ["+","-","*","/"]

    while True: 
        escolha = input("Escolha o operador: ")

        """A escolha do usuário está dentro da lista?"""
        if escolha in lista:
            return escolha
        

def ler_numeros()-> int|float:

    while True:
        
        a = input("Digite o primeiro número: ")
        b = input("Digite o segundo número: ")

        try:
            num1 = validar_entrada(a)
            num2 = validar_entrada(b)
            return num1, num2   
        
        except ValueError:
            print("Valor inválido")
        
def mostrar_resultado(resultado):
     print(f"Resultado: {resultado}")
        

     

    


