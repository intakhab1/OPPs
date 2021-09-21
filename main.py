

 # turtle library - python docs
 # import turtle
# bulli = turtle.Turtle()
# or
#
# from turtle import Turtle , Screen
# bulli = Turtle()
# print(bulli)
# bulli.shape("turtle")
# bulli.color("coral")
# bulli.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electro","Water","Fire"])
table.align = "l"
print(table)

