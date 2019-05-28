WIDTH = 800
HEIGHT = 600

pilka = Actor('ball')
paletka = Rect((WIDTH/2-100, HEIGHT-50), (200,25))
predkoscx = 5
predkoscy = 5
zycia = 5

def draw():
    screen.fill('white')
    pilka.draw()
    screen.draw.filled_rect(paletka, 'red')
    screen.draw.text(
        str(zycia),
        color='blue',
        midtop=(WIDTH // 2, 10),
        fontsize=30
    )

def on_mouse_move(pos):
    paletka.x = pos[0]

def update():
    global predkoscx, predkoscy, zycia

    pilka.x += predkoscx
    pilka.y += predkoscy

    if pilka.left < 0 or pilka.right > WIDTH:
        predkoscx = -predkoscx
    if pilka.top < 0 or pilka.colliderect(paletka):
        predkoscy = -predkoscy

    if pilka.top == HEIGHT:
        zycia -= 1
        pilka.top = 0
        pilka.left = 0

    if zycia < 1:
        predkoscx = 0
        predkoscy = 0