import tkinter as tk

"""Criar janela"""
janela = tk.Tk()

"Titulo da janela"
janela.title("Calculadora")

"""TAMANHO DA JANELA"""
janela.geometry("400x300")

"""COR DE FUNDO"""
janela.configure(bg="#f9d6d5")

"""PESO PARA JANELA: CRESCE OU DIMINUI CONFORME TAMANHO"""
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

retorno = tk.StringVar()

def adicionar_valor(valor):
    retorno.set(retorno.get() + str(valor))

"""TELA DE COMANDO"""
tela = tk.Entry(janela, font=("Roboto", 30), textvariable=retorno)
tela.grid(row=0, column=0, columnspan= 4, sticky="nsew", padx=20, pady=20)

"""FRAME TOPO"""
frame_topo = tk.Frame(janela,  bg="#f9d6d5")
frame_topo.grid(row=1, column=0, sticky="nsew")


"""FRAME DO MEIO"""
frame_meio = tk.Frame(janela, bg="#f9d6d5")
frame_meio.grid(row=2, column=0, sticky="nsew")

"""CONFIGURAÇÃO DA GRADE DA JANELA (PRINCIPAL)"""
janela.rowconfigure(0, weight=1)   #tela
janela.rowconfigure(1, weight=0)   # frame superior (operações)
janela.rowconfigure(2, weight=5)   # frame números (maior peso: MAIOR PARTE DA TELA, CRESCE MAIS)
janela.columnconfigure(0, weight=1)


"""BOTÕES 9 - 1"""
num = 9
for linha in range(3):
    for coluna in range(3):

        botao = tk.Button(
            frame_meio,
            text=num,
            font=("Roboto", 20, "bold"),
            bg="#fc6998",
            command=lambda num=num: adicionar_valor(num)
        )
        
        botao.grid(
            row=linha,
            column=coluna,
            padx=3,
            pady=3,
            sticky="nsew"     # ← ESSENCIAL PARA ESTICAR
        )

        num -= 1

"""BOTÃO 0"""
botao_0 = tk.Button(
    frame_meio,
    text="0",
    font=("Roboto", 20, "bold"),
    bg="#fc6998",
    command=lambda: adicionar_valor(0)
)
botao_0.grid(
    row=3,
    column=1,
    padx=5,
    pady=5,
    sticky="nsew"
)

"""BOTÃO SOMA"""
botao_soma = tk.Button(
    frame_meio,
    text="+",
    font=("Roboto", 20, "bold"),
    bg="#fa8fb1",
    command=lambda: adicionar_valor("+")

)

botao_soma.grid(
    row=0,
    column = 3,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

"""BOTÃO SUBTRAÇÃO"""
botao_subtracao= tk.Button(
    frame_meio,
    text="-",
    font=("Roboto", 20, "bold"),
    bg="#fa8fb1",
    command=lambda: adicionar_valor("-")   
)

botao_subtracao.grid(
    row=1,
    column = 3,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

"""BOTÃO MULTIPLICAÇÃO"""
botao_multiplicacao = tk.Button(
    frame_meio,
    text="*",
    font=("Roboto", 20, "bold"),
    bg="#fa8fb1",
    command=lambda: adicionar_valor("*")   
)

botao_multiplicacao.grid(
    row=2,
    column = 3,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

"""BOTÃO DIVISÃO"""
botao_divisao = tk.Button(
    frame_meio,
    text="/",
    font=("Roboto", 20, "bold"),
    bg="#fa8fb1",
    command=lambda: adicionar_valor("/")  
)

botao_divisao.grid(
    row=3,
    column = 3,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

"""FRAME DO MEIO RESPONSIVO"""
for coluna in range(4):            # 3 colunas
    frame_meio.columnconfigure(coluna, weight=1)

for linha in range(4):            # 4 linhas (3 + a linha do zero)
    frame_meio.rowconfigure(linha, weight=1)

def calcular_valor():

    try:
        resultado = eval(retorno.get())
        retorno.set(str(resultado))
    except Exception:
        retorno.set("Erro")

"""BOTÃO RESULTADO"""
botao_resultado = tk.Button(
    frame_topo,
    text="=",
    font=("Roboto", 20, "bold"),
    bg="#f74780",
    command=calcular_valor  
)

botao_resultado.grid(
    row=0,
    column = 2,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

def limpar():
    retorno.set("")

"""BOTÃO APAGAR: c"""
botao_c = tk.Button(
    frame_topo,
    text="C",
    font=("Roboto", 20, "bold"),
    bg="#f74780",
    command=limpar
    
)

botao_c.grid(
    row=0,
    column = 1,
    padx= 5,
    pady= 5,
    sticky="nsew"

)

"""FRAME DO TOPO RESPONSIVO"""
for coluna in range(3):
    frame_topo.columnconfigure(coluna, weight=1)
for linha in range(0):
    frame_topo.rowconfigure(linha,weight=1)

"""MAINLOOP: Sem mainloop() a janela abre e fecha na mesma hora.
"""
"""Sempre mover para a última linha do código"""
janela.mainloop()
