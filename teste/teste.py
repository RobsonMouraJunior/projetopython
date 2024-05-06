import turtle

def desenhar_coracao():
    tartaruga = turtle.Turtle()

    tartaruga.penup()
    tartaruga.goto(0, -200)
    tartaruga.pendown()

    tartaruga.begin_fill()
    tartaruga.fillcolor('red')
    tartaruga.left(140)
    tartaruga.forward(197)
    tartaruga.circle(-100, 200)
    tartaruga.left(120)
    tartaruga.circle(-100, 200)
    tartaruga.forward(197)
    tartaruga.end_fill()

    tartaruga.hideturtle()

def escrever_beatriz():
    tartaruga = turtle.Turtle()

    tartaruga.penup()
    tartaruga.goto(-150, 100)  # Posição inicial para o texto "Beatriz"
    tartaruga.pendown()

    tartaruga.color('black')
    tartaruga.hideturtle()

  # Texto a ser escrito
texto = "Beatriz"
    # Configurações da fonte
fonte = ("Arial", 60, "normal")
    # Espaçamento entre letras
espaço_letra = 50

    # Função para escrever uma letra do texto "Beatriz"
def escrever_letra(letra_idx):
        if letra_idx < len(texto):
            turtle.write(texto[letra_idx], align="left", font=fonte)
            # Agendando a escrita da próxima letra com um pequeno atraso
            turtle.ontimer(lambda: escrever_letra(letra_idx + 1), 300)  # Ajuste o tempo conforme desejado

    # Inicia a escrita da primeira letra
escrever_letra(0)

desenhar_coracao()
escrever_beatriz()

turtle.done()