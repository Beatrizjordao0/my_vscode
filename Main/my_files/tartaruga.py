import turtle

# Configuração da janela
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Desenhar o quadrado
quadrado = turtle.Turtle()

# Desenhar o quadrado
for _ in range(4):
    quadrado.forward(200)
    quadrado.left(90)

# Criar a bola
bola = turtle.Turtle()
bola.shape("circle")
bola.color("red")
bola.penup()  # Evita que a bola desenhe ao se mover
bola.goto(0, 0)  # Posiciona a bola no centro do quadrado

# Define a velocidade vertical da bola
bola.dy = -2

# Função para mover a bola
def mover():
    # Move a bola
    bola.sety(bola.ycor() + bola.dy)

    # Verifica se a bola atingiu a borda superior ou inferior do quadrado
    if bola.ycor() > 200 or bola.ycor() < -200:
        # Inverte a direção da bola
        bola.dy *= -1

    # Chama a função mover() repetidamente
    turtle.ontimer(mover, 100)

# Inicializa a função mover() para começar o movimento da bola
mover()

# Inicia o loop principal do Turtle
turtle.mainloop()
