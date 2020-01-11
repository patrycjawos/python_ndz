from random import randint
from time import sleep
import sys

TITLE = 'Snake'
WIDTH = 800
HEIGHT = 600

KROK = 50
kierunek = 'l'
przegrana = False
gra = False

snake = [Actor('snake_element', (WIDTH/2, HEIGHT/2))]
jablko = Actor('apple', (100, (randint(1,11)*50)))

przycisk_graj = Rect((WIDTH/2-100,HEIGHT-200), (200,50))
przycisk_wyjdz = Rect((WIDTH/2-100, HEIGHT-100), (200,50))

def draw():
    global gra
    screen.fill('black')

    if gra:
        for s in snake:
            s.draw()
        jablko.draw()

        if przegrana:
            screen.fill('black')
            screen.draw.text(
                str("LOSER"),
                color='white',
                midtop=(WIDTH // 2, 250),
                fontsize=100)
            sleep(2)
            gra = False

    else:
        screen.draw.filled_rect(przycisk_graj, 'green')
        screen.draw.filled_rect(przycisk_wyjdz, 'red')
        screen.draw.text(
            str("SNAKE"),
            color='white',
            midtop=(WIDTH // 2, 200),
            fontsize=100)
        screen.draw.text(
            str("Nacisnij klawisz SPACJA aby rozpoczac lub ESC zeby wyjsc z programu."),
            color='white',
            midtop=(WIDTH // 2, 300),
            fontsize=25)
        screen.draw.text(
            str("GRAJ"),
            color='white',
            center=(WIDTH/2, HEIGHT-175),
            fontsize=25)
        screen.draw.text(
            str("ZAKONCZ"),
            color='white',
            center=(WIDTH/2, HEIGHT-75),
            fontsize=25)

def on_key_down():
    global kierunek, gra
    if gra:
        if keyboard.right and kierunek != 'l':
            kierunek = 'p'
        if keyboard.left and kierunek != 'p':
            kierunek = 'l'
        if keyboard.up and kierunek != 'd':
            kierunek = 'g'
        if keyboard.down and kierunek != 'g':
            kierunek = 'd'
    else:
        if keyboard.space:
            gra = True
        if keyboard.escape:
            sys.exit()

def update():
    global przegrana, kierunek, snake
    if gra:
        if kierunek == 'l':
            snake.insert(0, Actor('snake_element', (snake[0].x - KROK, snake[0].y)))
        if kierunek == 'p':
            snake.insert(0, Actor('snake_element', (snake[0].x + KROK, snake[0].y)))
        if kierunek == 'g':
            snake.insert(0, Actor('snake_element', (snake[0].x, snake[0].y - KROK)))
        if kierunek == 'd':
            snake.insert(0, Actor('snake_element', (snake[0].x, snake[0].y + KROK)))

        if len(snake) > 3:
            snake.remove(snake[len(snake) - 1])

        for s in snake:
            if s.colliderect(jablko):
                if kierunek == 'l':
                    snake.append(Actor('snake_element', (snake[0].x - KROK, snake[0].y)))
                if kierunek == 'p':
                    snake.append(Actor('snake_element', (snake[0].x + KROK, snake[0].y)))
                if kierunek == 'g':
                    snake.append(Actor('snake_element', (snake[0].x, snake[0].y + KROK)))
                if kierunek == 'd':
                    snake.append(Actor('snake_element', (snake[0].x, snake[0].y - KROK)))
                jablko.x = randint(1, 15)*50
                jablko.y = randint(1, 11)*50

        for i in range(2, len(snake)):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                przegrana = True

        sleep(0.2)
    else:
        przegrana = False
        snake = [Actor('snake_element', (WIDTH/2, HEIGHT/2))]
        kierunek = 'l'

def on_mouse_down(pos):
    global gra
    if przycisk_graj.collidepoint(pos):
        gra = True
    elif przycisk_wyjdz.collidepoint(pos):
        sys.exit()