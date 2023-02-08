import turtle
import pandas

screen = turtle.Screen()


screen.title("U.S State Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

screen.tracer(0)

data = pandas.read_csv("50_states.csv")
statelist = []

for d in data["state"]:
    statelist.append(d)

guessed = 0

while guessed != 50:
    answerstate = turtle.textinput(title=f"{guessed}/50 guessed", prompt="Guess the state")
    if answerstate.title() in statelist:
        guessed+=1
        xcor = int(data[data["state"] == answerstate.title()].x)
        ycor = int(data[data["state"] == answerstate.title()].y)

        t = turtle.Turtle()
        t.hideturtle()
        screen.update()
        t.penup()
        t.speed(100)
        t.goto(xcor,ycor)
        t.write(answerstate.title(), font=("Courier",10,"normal"))

turtle.mainloop()