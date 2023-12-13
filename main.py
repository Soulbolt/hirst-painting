import random
import turtle
from turtle import Turtle, Screen

# import colorgram
#
# colors = colorgram.extract("hirst_painting.jpg", 20)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
color_list = [(249, 250, 252), (251, 249, 241), (252, 247, 251), (244, 251, 249), (244, 228, 79), (162, 75, 42),
              (216, 146, 90), (23, 30, 61), (124, 160, 218), (54, 89, 145), (45, 36, 30), (40, 48, 114), (29, 44, 34),
              (147, 56, 81), (131, 31, 43), (203, 82, 120), (146, 31, 25), (214, 80, 55), (69, 31, 41), (67, 113, 77)]
leo = Turtle()
leo.pensize(20)
leo.hideturtle()

# leo.setheading(225)
# leo.forward(300)
# leo.setheading(0)


def dots_painting(size):
    increase = 0
    move_up = 0
    for _ in range(size):
        increase += 1
        leo.dot(20, random.choice(color_list))
        leo.penup()
        leo.forward(50)
        leo.pendown()
        if increase == 10:
            move_up += 1
            increase = 0
            leo.penup()
            leo.goto(0, 30 * move_up)
            leo.pendown()


dots_painting(100)

screen = Screen()
screen.exitonclick()
