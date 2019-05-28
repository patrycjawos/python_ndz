WIDTH = 800
HEIGHT = 600

alien = Actor('alien')

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    alien.top += 2
    if alien.top > HEIGHT:
        alien.pos = (0,0)

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
#        sounds.eep.play()
#        alien.image = 'alien_hurt'
#        print("Aj!")
#    else:
#        print("Nie trafiles!")

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'