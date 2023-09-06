import turtle
import time
import pandas
screen = turtle.Screen()
img = "Vietnam_location_map.gif"
screen.addshape(img)
turtle.shape(img)
screen.title("Vietnam_map_game")
screen.setup(1.0, 1.0)

data = pandas.read_csv("63_province.csv")
all_province = data.Name.to_list()
user_answer = []

while len(user_answer) < 63:
    missing_province = []
    answer_province = screen.textinput(f"{len(user_answer)}/63 Province Correct", "What's another province's Name?").title()
    if answer_province == "Exit":
        for province in all_province:
            if province not in user_answer:
                missing_province.append(province)
        miss_data = pandas.DataFrame(missing_province)
        miss_data.to_csv("province_to_learn.csv")
        break
    if answer_province in all_province:
        user_answer.append(answer_province)
        province_data = data[ data.Name == answer_province]
        print(province_data)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.goto(int(province_data.X), int(province_data.Y))
        new_turtle.hideturtle()
        new_turtle.write( answer_province, False, 'Center', ("Courier", 5, "normal"))


