# Written 7/25/2022
# Day 25 Project of 100 Days of Code

# Program that emulates the US State name game, tests pandas dataframe comprehension and turtle graphics

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

print(data)
# check if value matches,  
correct_guesses = []
all_states = data.state.tolist()
print(all_states)
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title = f"{len(correct_guesses)}/50 States Correct", prompt="What state would you like to guess?").title()
    if answer_state == "Exit":
        exit_data = pd.DataFrame(set(all_states) ^ set(correct_guesses))
        exit_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states: 
        t = turtle.Turtle(); t.hideturtle(); t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        correct_guesses.append(answer_state)
