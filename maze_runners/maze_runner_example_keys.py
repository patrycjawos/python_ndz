
TITLE = 'Maze runner'
WIDTH = 600
HEIGHT = 800

RUCH = 5
CZERWONY = (255,0,0)

alien = Actor('alien', anchor=('center', 'center'))

sciana_labirynt_1 = Rect((200, 150), (20, 250))
sciana_labirynt_2 = Rect((400, 300), (20, 250))

sciany = [sciana_labirynt_1, sciana_labirynt_2]

def draw():
    screen.fill('black')
    for s in sciany:
        screen.draw.filled_rect(s, CZERWONY)
    alien.draw()


def update():
    if keyboard.left:
        alien.x -= RUCH
    elif keyboard.right:
        alien.x += RUCH
    elif keyboard.up:
        alien.y -= RUCH
    elif keyboard.down:
        alien.y += RUCH