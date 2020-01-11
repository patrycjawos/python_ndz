from random import randint
from time import sleep

TITLE = 'Snake'
WIDTH = 800
HEIGHT = 600

KROK = 50
kierunek = 'l'
przegrana = False

snake = [Actor('snake_element', (WIDTH/2, HEIGHT/2))]
jablko = Actor('apple', (100, (randint(1,11)*50)))

def draw():
    screen.fill('black')
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

def on_key_down():
    global kierunek
    if keyboard.right and kierunek != 'l':
        kierunek = 'p'
    if keyboard.left and kierunek != 'p':
        kierunek = 'l'
    if keyboard.up and kierunek != 'd':
        kierunek = 'g'
    if keyboard.down and kierunek != 'g':
        kierunek = 'd'

def update():
    global kierunek, przegrana

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