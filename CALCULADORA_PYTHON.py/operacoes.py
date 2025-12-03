def soma(a,b) -> int | float:
    
    try:
        return a + b

    except (ValueError, TypeError):
       print("Digite apenas números")

           

def sub(a,b) -> int | float:
   
    try:
        return a - b

    except  (ValueError, TypeError):
       print("Digite apenas números")
 

def mult(a,b) -> int | float:

    try:
       return a * b

    except  (ValueError, TypeError):
       print("Digite apenas números")

 
def div(a,b) -> int | float:

    try:
        return a / b

    except ZeroDivisionError:
        print("Não é possivel dividir por zero")
