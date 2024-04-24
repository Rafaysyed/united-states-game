import turtle
import pandas

screen = turtle.Screen()
screen.title('United States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt="What is another state name? ").title()
data = pandas.read_csv("50_states.csv")
states = data.state.tolist()

text_turtle = turtle.Turtle()
text_turtle.penup()
text_turtle.hideturtle()

game_on = True
count = 0

while game_on:
    if answer_state in states:
        # Find the row corresponding to the answer_state
        row_data = data[data.state == answer_state]

        # Extract the x and y coordinates from the row_data
        x_coord = row_data.x.iloc[0]
        y_coord = row_data.y.iloc[0]

        text_turtle.goto(x_coord, y_coord)
        text_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))

        print("found")
        count += 1
        states.remove(answer_state)  # Remove the state from the list to prevent duplicate entries

    answer_state = screen.textinput(title=f"Guess the state {count}/50", prompt="What is another state name? ").title()

    # Check if the game is completed
    if count == 50:
        game_on = False

screen.exitonclick()

