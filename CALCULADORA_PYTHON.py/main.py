from interface import menu_operadores, ler_operador, ler_numeros, mostrar_resultado
from operacoes import soma, sub, mult, div

def main():

    while True:
        
        menu_operadores()
        operador = ler_operador()
        a,b = ler_numeros()

        if operador == "+":
            resultado = soma(a,b)
        elif operador == "-":
            resultado =sub(a,b)
        elif operador == "*":
            resultado =mult(a,b)
        elif operador == "/":
            resultado =div(a,b)

        mostrar_resultado(resultado)
        print("Deseja continuar? ")
        escolha = input("Digite 1 para SIM e 2 para NÃO: ")

        if escolha ==  "2":
            break
        

if __name__ == "__main__":
    main()

    
    
