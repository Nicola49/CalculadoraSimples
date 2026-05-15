from tkinter import *
from tkinter import ttk

todos_valores = ''

def calcular():
    global todos_valores
    try:
        a = eval(todos_valores)
    except:
        valor_texto.set('ERRO!')
        todos_valores = ''
    else:
        todos_valores = str(a)
        valor_texto.set(todos_valores)

def escrever_n(n):
    global todos_valores
    todos_valores = todos_valores + str(n)
    valor_texto.set(todos_valores)

def deletar_n():
    global todos_valores
    todos_valores = todos_valores[0:-1]
    valor_texto.set(todos_valores)

def clean():
    global todos_valores
    todos_valores = ''
    valor_texto.set(todos_valores)

cor1 = "#A0522D"
cor2 = "#F5F5DC"
cor3 = "#F4A460"
cor4 = "#E35336"
cor5 = "#000000"

janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor5)

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

valor_texto = StringVar()

label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor1, fg='white')
label.place(x=0, y=0)

b1 = Button(frame_corpo, text='C', width=11, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=clean)
b1.place(x=0, y=0)
b2 = Button(frame_corpo, text='%', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('%'))
b2.place(x=118, y=0)
b3 = Button(frame_corpo, text='/', width=5, height=2, bg=cor3, fg='white', font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('/'))
b3.place(x=177, y=0)

b4 = Button(frame_corpo, text='7', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('7'))
b4.place(x=0, y=52)
b5 = Button(frame_corpo, text='8', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('8'))
b5.place(x=59, y=52)
b6 = Button(frame_corpo, text='9', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('9'))
b6.place(x=118, y=52)
b7 = Button(frame_corpo, text='*', width=5, height=2, bg=cor3, fg='white', font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('*'))
b7.place(x=177, y=52)

b8 = Button(frame_corpo, text='4', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('4'))
b8.place(x=0, y=104)
b9 = Button(frame_corpo, text='5', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('5'))
b9.place(x=59, y=104)
b10 = Button(frame_corpo, text='6', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('6'))
b10.place(x=118, y=104)
b11 = Button(frame_corpo, text='-', width=5, height=2, bg=cor3, fg='white', font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('-'))
b11.place(x=177, y=104)

b12 = Button(frame_corpo, text='1', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('1'))
b12.place(x=0, y=156)
b13 = Button(frame_corpo, text='2', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('2'))
b13.place(x=59, y=156)
b14 = Button(frame_corpo, text='3', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('3'))
b14.place(x=118, y=156)
b15 = Button(frame_corpo, text='+', width=5, height=2, bg=cor3, fg='white', font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('+'))
b15.place(x=177, y=156)

bdel = Button(frame_corpo, text='⌫', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=deletar_n)
bdel.place(x=0, y=208)
b16 = Button(frame_corpo, text='0', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('0'))
b16.place(x=59, y=208)
b17 = Button(frame_corpo, text='.', width=5, height=2, bg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: escrever_n('.'))
b17.place(x=118, y=208)
b18 = Button(frame_corpo, text='=', width=5, height=2, bg=cor3, fg='white', font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=calcular)
b18.place(x=177, y=208)

janela.mainloop()