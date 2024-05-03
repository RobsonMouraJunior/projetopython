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
    tartaruga.goto(0, 100)
    tartaruga.pendown()

    tartaruga.color('black')

    # Função para animar o texto
    def animar_texto():
        tartaruga.write("Beatriz", align="center", font=("Arial", 20, "normal"))

    # Agendar a animação do texto após um curto atraso
    turtle.ontimer(animar_texto, 1000)

    tartaruga.hideturtle()

desenhar_coracao()
escrever_beatriz()

turtle.done()
