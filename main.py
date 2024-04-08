# Instruções do exercicio: Usando seus conhecimentos aprendidos em sala, realize uma interface de login utilizando a biblioteca Tkinter em Python. O objetivo é permitir que o usuário faça login somente se a senha tiver mais de 6 dígitos e se o e-mail contiver o caractere "@", ou seja, realizar uma tela de login com restrições de e-mail e senha.

import tkinter as tk
from tkinter import messagebox

def fazer_login():
    email = entrada_email.get()
    senha = entrada_senha.get()

    if '@' not in email:
        messagebox.showerror("Erro de Login", "Por favor, insira um e-mail válido.")
    elif len(senha) <= 6:
        messagebox.showerror("Erro de Login", "A senha deve ter mais de 6 dígitos.")
    else:
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")

# janela
janela = tk.Tk()
janela.title("Tela de Login")

tk.Label(janela, text="Login:", font=("Arial", 16, "bold")).pack()

# e-mail
tk.Label(janela, text="Insira seu e-mail:").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

# senha
tk.Label(janela, text="Insira sua senha:").pack()
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

# login
botao_login = tk.Button(janela, text="Fazer Login", command=fazer_login)
botao_login.pack()


janela.mainloop()
