import pgzrun
import random
WIDTH = 700
HEIGHT = 700
race = Actor("")
race.pos = 600, 600
life=5
vehicles=["yc", "truck", "policar"]
cars=[]
powers=["po", "f"]
pows=[]
lane_width=250
num_lanes=3
lane_centers = [lane_width // 2 + lane_width * i for i in range(num_lanes)]
print(lane_centers)
sounds.racecar.play(-1)
bg_x=0
bg_y=-200
def spawn():
    ranom=Actor(random.choice(vehicles))
    ranom.x=random.choice(lane_centers)
    ranom.y=-10
    cars.append(ranom)
def power():
    p=Actor(random.choice(powers))
    p.x=random.choice(lane_centers)
    p.y=-10
    pows.append(p)
def update():
    global bg_y
    if keyboard.a:
        race.x -= 5
    elif keyboard.d:
        race.x += 5
    for car in cars:
        car.y+=random.randint(7, 15)
    for pow in pows:
        pow.y+=random.randint(3, 7)
    bg_y+=4
    if abs(bg_y)<100:
       bg_y=-300 
    check_collision() 
def draw():
    screen.fill("black")
    screen.blit("tr", (bg_x, bg_y))
    race.draw()
    for car in cars:
        car.draw()
    for pow in pows:
        pow.draw()
    if life>=20:
        screen.blit("win", (0, 0))
        screen.draw.text("You WIN", (640, 10))
    screen.draw.text("Life", (653, 10), color="dark green" )
    screen.draw.text("={}".format(life), (653, 23), color="dark green" )
def check_collision():
    global life
    for car in cars:
        if car.colliderect(race):
            cars.remove(car)
            life=life-1
            sounds.sc.play()
    for pow in pows:
        if pow.colliderect(race):
            pows.remove(pow)            
            life=life+1
            sounds.beep.play()       
clock.schedule_interval(spawn, 2)
clock.schedule_interval(power, 2)
pgzrun.go()