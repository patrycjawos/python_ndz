import random

WIDTH = 600
HEIGHT = 600

przycisk = Rect((WIDTH/2-100, 100), (200,75))

odpowiedzi = ["Moj wywiad donosi: NIE", "Wyglada dobrze", "Kto wie?", "Zapomnij o tym", "Tak - w swoim czasie",
            "Prawie jak tak", "Nie teraz", "YES, YES, YES", "To musi poczekac", "Mam pewne watpliwosci",
            "Mozesz na to liczyc", "Zbyt wczesnie aby powiedziec", "Daj spokoj", "Absolutnie", "Chyba zartujesz?",
            "Na pewno nie", "Zrob to", "Prawdopodobnie", "Dla mnie rewelacja", "Na pewno tak"]

odpowiedz = ""

def draw():
    screen.blit('8ball', (0,0))
    screen.draw.filled_rect(przycisk, 'blue')
    screen.draw.text(
        "Zadaj na glos pytanie i popros kule o odpowiedz!",
        color='blue',
        midtop=(WIDTH/2,50),
        fontsize=25)
    screen.draw.text(
        "Odpowiedz",
        color='white',
        center=przycisk.center,
        fontsize=25)
    screen.draw.text(
        str(odpowiedz),
        color='red',
        center=(WIDTH/2, HEIGHT/2),
        fontsize=35,
        shadow=(1,1))

def on_mouse_down(pos):
    global odpowiedz
    if przycisk.collidepoint(pos):
        odpowiedz = random.choice(odpowiedzi)