#---------------------------SET UP---------------------------

#Importing Turtle Random modules
import turtle as trtl
import random as rand

#Creating screen and background
wn = trtl.Screen()
trtl.screensize(canvwidth=640, canvheight=980)
wn.title("Flappy Bird --- By Haley and Jane  P:6")
wn.bgpic("background.png")

#Creating Flappy Bird Object
flappy_bird = trtl.Turtle()
flappy_bird.speed(50)
flappy_bird.penup()
flappy_bird.setposition(-150,0)
flappy_bird.dy = 1 
player_score = 0
game_not_over = "yes"

#Making it a Flappy Bird with Image
wn.addshape('stand-still_bird.gif')
flappy_bird.shape('stand-still_bird.gif')

#Creating Score Turtle
score = trtl.Turtle()
score.speed(20)
score.hideturtle()
score.penup()
score.color("white")

#Ask User Prompt or Write Score
def write_score(isScore = True):
  score.goto(-300, 70)
  if isScore:
    score.write("Score", move=False, align="left", font=("Verdana", 20, "normal"))
    score.goto(-300, 30)
    score.write(player_score, move=False, align="left", font=("Verdana", 30, "bold"))
  else:
    score.write("Press Space to Jump!", move=False, align="left", font=("Verdana", 20, "normal"))
#Ask User Prompt (Space) for jump
write_score(False)

#Cloud and Star Lists
sky_objects = []
cloud_or_star = []
clouds_and_stars = ['cloud1.gif', 'cloud2.gif','cloud3.gif','cloud4.gif', 'cloud5.gif', 'star1.gif','star2.gif','star3.gif']

#Obstacle list
obstacles_down = []
pipe_down = []
obstacles_up = []
pipe_up = []
obstacle_list = ['pipe_down.gif','pipe_up.gif']
#---------------------------FUNCTIONS---------------------------
#adding more turtles and assigning gifs to each turtle
for i in range(4):
  sky_objects.append(trtl.Turtle())
  cloud_or_star.append(rand.choice(clouds_and_stars))

#Creating Pipes down
for i in range(2):
  obstacles_down.append(trtl.Turtle())
  pipe_down.append(obstacle_list[0])

#Creating Pipes Up
for i in range(2):
  obstacles_up.append(trtl.Turtle())
  pipe_up.append(obstacle_list[1])

# adding cloud image to the background
def make_cloud(index):
  sky_objects[index].hideturtle()
  sky_objects[index].pu()
  sky_objects[index].setx (rand.randint(400,600))
  sky_objects[index].sety (rand.randint(200,400))
  sky_objects[index].speed(10)
  wn.addshape(cloud_or_star[index])
  sky_objects[index].shape(cloud_or_star[index])

# adding down obstacle image to the background
def make_obstacle_down(index):
  obstacles_down[index].hideturtle()
  obstacles_down[index].pu()
  obstacles_down[index].setx (index*200 + 400)
  obstacles_down[index].sety (350)
  obstacles_down[index].speed(30)
  wn.addshape(pipe_down[index])
  obstacles_down[index].shape(pipe_down[index])
  obstacles_down[index].showturtle()

# adding up obstacle image to the background
def make_obstacle_up(index):
  obstacles_up[index].hideturtle()
  obstacles_up[index].pu()
  obstacles_up[index].setx (index*200 + 400)
  obstacles_up[index].sety (-125)
  obstacles_up[index].speed(30)
  wn.addshape(pipe_up[index])
  obstacles_up[index].shape(pipe_up[index])
  obstacles_up[index].showturtle()

# making the clouds move backward
#use if statement to move turtle
def clouds_moves(index):
  if sky_objects[index].xcor() > -400:
    sky_objects[index].showturtle()
    sky_objects[index].backward(25)
  else:
    sky_objects[index].clear()
    wn.addshape(cloud_or_star[index])
    sky_objects[index].shape(cloud_or_star[index])
    sky_objects[index].setx (rand.randint(400,600))
    sky_objects[index].sety (rand.randint(200,400))

# making the down obstacles move and reset
def obstacles_down_moves(index):
  if obstacles_down[index].xcor() > -400:
    obstacles_down[index].showturtle()
    obstacles_down[index].backward(25)
  else:
    obstacles_down[index].clear()
    wn.addshape('pipe_down.gif')
    obstacles_down[index].shape('pipe_down.gif')
    obstacles_down[index].setx(250)
    obstacles_down[index].sety(350)

#making the up obstacles move and reset
def obstacles_up_moves(index):      
  if obstacles_up[index].xcor() > -400:
    obstacles_up[index].showturtle()
    obstacles_up[index].backward(25)
  else:
    obstacles_up[index].clear()
    wn.addshape('pipe_up.gif')
    obstacles_up[index].shape('pipe_up.gif')
    obstacles_up[index].setx (250)
    obstacles_up[index].sety (-125)

def game_over ():
  global game_not_over, player_score
  if player_score == 4.75:
    score.clear()
    player_score = 0
    write_score()
  game_not_over = "no, it's over"
  flappy_bird.hideturtle()
  score.setposition(0,0)
  score.write("GAME OVER", move=False, align="center", font=("Verdana", 30, "bold"))
  wn.update()

# when flappy bird reaches certain x and y coordinates, reset the game with the game_over function
def when_game_over(index): 
  if (flappy_bird.xcor() + 10  > obstacles_up[index].xcor() - 50) and ((flappy_bird.ycor()) - 10 < obstacles_up[index].ycor() + 200):
    game_over()

  if (flappy_bird.xcor() +10  > obstacles_down[index].xcor() - 50) and ((flappy_bird.ycor()) + 10 > obstacles_down[index].ycor() -170):  
    game_over()
    
def update_score():
  global player_score
  player_score += 0.25
  score.clear()
  write_score()
    
#Makes the wings of the Flappy Bird Flap
def wing_flap():
    flappy_bird.shape('stand-still_bird.gif')
    flappy_bird.dy -= 0.5
    wn.addshape('flapping_bird.gif')
    flappy_bird.shape('flapping_bird.gif')
    flappy_bird.dy += 0.5

#Makes the Flappy Bird Flap Go Up and "jump"
def jump():
  wing_flap()
  flappy_bird.dy += 8 
  if flappy_bird.dy > 8:
    flappy_bird.dy = 8

#---------------------------CALL FUNCTIONS---------------------------

for i in range(4):
  make_cloud(i)

for i in range(2): 
  make_obstacle_down(i)
  make_obstacle_up(i)

# User Input
wn.listen()
wn.onkeypress(jump, "space")

while True:
  flappy_bird.dy -= 0.05
  wn.update()
  flappy_bird.dy += 0.05
  # Downward force on the flappy bird
  flappy_bird.dy += -0.4 
  #Moves Flappy Bird/Allows Flappy Bird to Move
  flappy_bird.sety(flappy_bird.ycor() + flappy_bird.dy)
  # Stops flappy bird from leaving the screen
  if flappy_bird.ycor() < -290:
      flappy_bird.dy = 0
      flappy_bird.sety(-290)
      flappy_bird.shape('stand-still_bird.gif')
  #Allows Clouds to Move
  for i in range(4):
    clouds_moves(i)
  #Allows Obstacles to Move
  for i in range(2):
    obstacles_down_moves(i)
    obstacles_up_moves(i)
    when_game_over(i)
  if game_not_over == "yes":
      update_score()

#Window
wn.mainloop()