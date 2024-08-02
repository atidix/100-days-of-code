import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "day-25/India-States-Game/state_map.gif"
screen.addshape(image)

turtle.shape(image)

def keep_guessing():
    return screen.textinput(f"{len(guessed_states)}/36 Correct", "What's another state's name?")

data = pandas.read_csv("day-25/India-States-Game/36.csv")
tim = turtle.Turtle()
all_states = data.state.to_list()
guessed_states = []
game_on = True

while game_on == True:
    answer_state = keep_guessing()
    guess = answer_state.title()
    if guess == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if guessed_states not in all_states:
        #         missing_states.append(state)
        #         print(missing_states)
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
        if len(guessed_states) == 36:
            game_on = False
            print("You Win!")


turtle.mainloop()