from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Люто абезянки пинг-понг")

background = GameSprite('fon.jpg', 0, 0, 0, win_width, win_height)

game = True
finish = False
clock = time.Clock()
clock.tick(60)
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    if finish == False:
        background.reset()

    display.update()
    clock.tick(FPS)