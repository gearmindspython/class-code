import random

TITLE = 'Flappy Bird'
WIDTH = 400
HEIGHT = 708

barry.speed = 1

gap = 140
top_pipe = Actor('top', (300, 0))
bottom_pipe = Actor('bottom', (300, top_pipe.height + gap))

scroll_speed = -1
gravity = 0.3

reset()
barry.score = 0

def update():
    # moving barry the bird
    barry.speed += gravity
    barry.y += barry.speed

    # moving the pipes
    top_pipe.x += scroll_speed
    bottom_pipe.x += scroll_speed

    # pipes off screen?
    if top_pipe.right < 0:
        offset = random.randint(-150, 0)
        top_pipe.midleft = (WIDTH, offset)
        bottom_pipe.midleft = (WIDTH, offset + top_pipe.height + gap)

    # barry the bird off screen?
    if barry.y > HEIGHT or barry.y < 0:
        reset()

    # if we hit the pipe
    if (barry.colliderect(top_pipe) or barry.colliderect(bottom_pipe)):
        hit_pipe()

    # changing score
    if top_pipe.right < barry.x:
        barry.score += 1

    # animation
    if barry.alive:
        if barry.speed > 0:
            barry.image = 'bird1'
        else:
            barry.image = 'bird0'

def on_mouse_down():
    if barry.alive:
        barry.speed = -6.5

def reset():
    print('Back to the start....')
    barry.speed = 1
    barry.center = (75, 350)
    barry.image = 'bird1'
    top_pipe.center = (300, 0)
    bottom_pipe.center = (300, top_pipe.height + gap)
    top_pipe.pair_number = 1
    barry.alive = True

def hit_pipe():
    print("You hit the pipe.")
    barry.image = 'birddead'
    barry.alive = False

def draw():
    screen.blit('background', (0, 0))
    barry.draw()
    top_pipe.draw()
    bottom_pipe.draw()

    screen.draw.text(
    str('high score'),
    color = 'white',
    midtop = (20, 10),
    fontsize = 30,
    )barry = Actor('bird1', (75, 350))