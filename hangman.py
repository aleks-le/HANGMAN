from turtle import*

speed(0)
delay(0)

def hangman_tyhi():
    up()
    left(90)
    forward(170)
    left(90)
    forward(180)
    left(180)
    down()
    forward(250)
    left(90)
    forward(15)
    left(90)
    forward(250)
    left(90)
    forward(15)
    left(90)
    forward(15)
    right(90)
    forward(350)
    left(90)
    forward(25)
    left(90)
    forward(350)
    right(90)
    forward(165)
    right(90)
    forward(80)

def hangman_pea():
    hangman_tyhi()
    right(90)
    circle(30)

def hangman_k2si():
    hangman_pea()
    up()
    left(90)
    forward(60)
    down()
    right(60)
    forward(70)
    left(180)
    forward(70)

def hangman_k2si2():
    hangman_k2si()
    right(60)
    forward(70)
    left(180)
    forward(70)

def hangman_keha():
    hangman_k2si2()
    left(120)
    forward(90)

def hangman_jalg():
    hangman_keha()
    right(30)
    forward(90)
    left(180)
    forward(90)
    
def hangman_jalg2():
    hangman_jalg()
    right(120)
    forward(90)


exitonclick()