WIDTH = 800
HEIGHT = 600

RUCH = 5
CZERWONY = (255,0,0)

alien = Actor('alien', anchor=('center', 'center'))

alien.poprzedni_x = alien.center
alien.poprzedni_y = alien.center

gorna_sciana = Rect((0,0), (WIDTH, 30))
dolna_sciana = Rect((0,HEIGHT-30), (WIDTH,30))
lewa_sciana_gora = Rect((0,0), (30, HEIGHT/2-60))
lewa_sciana_dol= Rect((0,HEIGHT/2+60), (30, HEIGHT/2-60))
prawa_sciana_gora = Rect((WIDTH-30, 0), (30, HEIGHT/2-60))
prawa_sciana_dol = Rect((WIDTH-30, HEIGHT/2+60), (30, HEIGHT/2-60))

sciana_labirynt_1 = Rect((200, 150), (20, 250))
sciana_labirynt_2 = Rect((400, 300), (20, 250))
sciana_labirynt_3 = Rect((600, 150), (20, 250))

koniec = Rect((WIDTH-10, HEIGHT/2-60), (10, 120))

sciany = [gorna_sciana, dolna_sciana, lewa_sciana_gora, lewa_sciana_dol, prawa_sciana_gora, prawa_sciana_dol, sciana_labirynt_1, sciana_labirynt_2, sciana_labirynt_3]

def draw():
    screen.fill('black')
    for s in sciany:
        screen.draw.filled_rect(s, CZERWONY)
    alien.draw()

    if alien.colliderect(koniec):
        screen.fill('green')
        screen.draw.text(
            str("WINNER"),
            color='white',
            midtop=(WIDTH // 2, 250),
            fontsize=100)

def update():

    lista_zderzen = alien.collidelistall(sciany)

    for i in lista_zderzen:
        if alien.x != alien.poprzedni_x:
            if alien.x < alien.poprzedni_x:
                alien.left = sciany[i].right
            else:
                alien.right = sciany[i].left

        elif alien.y != alien.poprzedni_y:
            if alien.y < alien.poprzedni_y:
                alien.top = sciany[i].bottom
            else:
                alien.bottom = sciany[i].top

    if keyboard.left:
        alien.poprzedni_x = alien.x
        alien.x -= RUCH

    if keyboard.right:
        alien.poprzedni_x = alien.x
        alien.x += RUCH

    if keyboard.up:
        alien.poprzedni_y = alien.y
        alien.y -= RUCH

    if keyboard.down:
        alien.poprzedni_y = alien.y
        alien.y += RUCH