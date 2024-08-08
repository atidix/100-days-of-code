import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day-25/US-States-Game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def keep_guessing():
    return screen.textinput(f"{len(guessed_states)}/50 Correct", "What's another state's name?")

data = pandas.read_csv("day-25/US-States-Game/50_states.csv")
tim = turtle.Turtle()
guessed_states = []
all_states = data.state.to_list()
game_on = True

while game_on == True:
    answer_state = keep_guessing()
    guess = answer_state.title()
    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        break
    check = data[data.state == guess]
    if not check.empty:
        x_coor = check.x.item()
        y_coor = check.y.item()
        tim.hideturtle()
        tim.penup()
        tim.goto(x_coor,y_coor)
        tim.write(guess)
        guessed_states.append(guess)
        if len(guessed_states) == 50:
            game_on = False
            print("You Win!")

turtle.mainloop()