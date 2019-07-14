import pgzrun

WIDTH = 144
HEIGHT = 256

player = Actor("bird", (20, 128))

def draw():
    player.draw()


pgzrun.go()