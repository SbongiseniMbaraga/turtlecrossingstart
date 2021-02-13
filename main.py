import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# player moves forward and bind key to method
player = Player()
screen.listen()
screen.onkey(player.move_forward, "Up")

# cars are generated
cars = CarManager()

# score
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_design_position_and_new_car()
    cars.car_movement()
    # when player is clear, give point and reset position
    if player.ycor() == 300:
        scoreboard.add_score()
        player.reset_position()
        cars.car_movement_speed()
    # if the player touches one of the cars then game over
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
