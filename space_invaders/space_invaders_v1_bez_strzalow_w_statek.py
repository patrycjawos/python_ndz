WIDTH = 800
HEIGHT = 600

PREDKOSC_STATKU = 50
predkosc_wrogow = 2

statek = Actor('player_ship', midbottom=(WIDTH/2, HEIGHT-50))
wrogowie = []
lasery = []

# tworzenie wrogow
for x in range(0,5):
    wrogowie.append(Actor('enemy', (x*WIDTH/5+80, 80)))

def draw():
    screen.fill('black')
    statek.draw()
    for w in wrogowie:
        w.draw()
    for l in lasery:
        l.draw()
    if len(wrogowie) == 0:
        screen.draw.text(
            "WINNER",
            color='white',
            center=(WIDTH/2,HEIGHT/2),
            fontsize=100)

def on_key_down():
    if keyboard.left:
        statek.x -= PREDKOSC_STATKU
    elif keyboard.right:
        statek.x += PREDKOSC_STATKU

def update():
    if len(wrogowie) > 0:
        animacja()
    if keyboard.space:
        lasery.append(Actor('laser', (statek.midtop)))
    for l in lasery:
        l.y -= 5
        for w in wrogowie:
            if l.colliderect(w):
                wrogowie.remove(w)

def animacja():
    global predkosc_wrogow
    for w in wrogowie:
        w.x += predkosc_wrogow
    if wrogowie[0].left <= 0 or wrogowie[len(wrogowie) - 1].right >= WIDTH:
        predkosc_wrogow  = -predkosc_wrogow