from tkinter import *


def retorna_lista():
    logins = {}
    return logins


logins = retorna_lista()


def cadastro():
    def on_click():
        logins[edLogin.get()] = edNome.get(), edLogin.get(), edSenha.get(), edEmail.get()
        lb6 = Label(janelaCadastro, text="USUÁRIO CADASTRADO", background="SlateBlue1", width="50", height="2")
        lb6.grid(row=4, column=0, columnspan=10, sticky=W + E)
        return logins

    janelaCadastro = Tk()
    janelaCadastro['background'] = "Plum"
    lb = Label(janelaCadastro, text="Nome", background="SlateBlue1", width="6", height="1")
    lb2 = Label(janelaCadastro, text="Login", background="SlateBlue1", width="6", height="1")
    lb3 = Label(janelaCadastro, text="Senha", background="SlateBlue1", width="6", height="1")
    lb4 = Label(janelaCadastro, text="E-mail", background="SlateBlue1", width="6", height="1")

    edNome = Entry(janelaCadastro, background="MediumPurple")
    edLogin = Entry(janelaCadastro, background="MediumPurple")
    edSenha = Entry(janelaCadastro, background="MediumPurple")
    edEmail = Entry(janelaCadastro, background="MediumPurple")

    btCadastro = Button(janelaCadastro, text="Finalizar cadastro", background="SlateBlue1",
                        command=on_click)
    btVoltar = Button(janelaCadastro, text="Voltar", background="SlateBlue1", command=janelaCadastro.destroy)

    lb.grid(row=0, column=0, sticky=W)
    lb2.grid(row=1, column=0, sticky=W)
    lb3.grid(row=2, column=0, sticky=W)
    lb4.grid(row=3, column=0, sticky=W)

    edNome.grid(row=0, column=1)
    edLogin.grid(row=1, column=1)
    edSenha.grid(row=2, column=1)
    edEmail.grid(row=3, column=1)

    btCadastro.grid(row=5, column=0)
    btVoltar.grid(row=5, column=1)

    janelaCadastro.geometry("500x200+700+300")
    janelaCadastro.mainloop()


def msgError():
    janelaAcesso = Tk()
    janelaAcesso['background'] = 'Coral'
    msgError = Label(janelaAcesso, text="USUÁRIO OU SENHA INVÁLIDO", background="DarkSalmon")
    btvoltar = Button(janelaAcesso, text="Tentar Novamente", background="DarkSalmon", command=janelaAcesso.destroy)
    msgError.place(x=170, y=70)
    btvoltar.place(x=200, y=100)

    janelaAcesso.geometry("500x200+700+300")
    janelaAcesso.mainloop()


def janela_principal():
    def on_bt():
        if len(logins) == 0:
            msgError()

        if ed1.get() in logins:
            if ed2.get() in logins[ed1.get()]:
                janelaAcesso = Tk()
                janelaAcesso['background'] = 'LightGreen'
                msgLogin = Label(janelaAcesso, text="VOCÊ ESTÁ LOGADO", background="SpringGreen")
                msgLogin.place(x=170, y=70)
                janelaAcesso.geometry("500x200+700+300")
                janelaAcesso.mainloop()
            else:
                msgError()
        else:
            msgError()

    janela = Tk()
    janela['background'] = 'SlateBlue3'
    lb1 = Label(janela, text="Login: ", background="SlateBlue1")
    lb2 = Label(janela, text="Senha: ", background="SlateBlue1")

    ed1 = Entry(janela, background="MediumPurple")
    ed2 = Entry(janela, background="MediumPurple")

    bt1 = Button(janela, text="Entrar", background="SlateBlue1", command=on_bt)
    bt2 = Button(janela, text="Cadastrar", background="SlateBlue1", command=cadastro)

    lb1.place(x=170, y=70)
    lb2.place(x=170, y=100)

    ed1.place(x=220, y=70)
    ed2.place(x=220, y=100)
    bt1.place(x=220, y=125)
    bt2.place(x=270, y=125)

    janela.geometry("500x200+700+300")
    janela.mainloop()


janela_principal()
