from pygame import *

window=display.set_mode((700, 500))

display.set_caption('Догонятор3000')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect_x = player_x
        self.rect_y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect_x, self.rect_y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys[K_RIGHT] and self.rect_x < 620:
            self.rect_x += self.speed
        if keys[K_UP] and self.rect_y > 5:
            self.rect_y -= self.speed
        if keys[K_DOWN] and self.rect_y < 420:
            self.rect_y += self.speed

class Enemy(GameSprite):
    flag = "left"
    def update(self):
        if self.rect_x <= 470:
            self.flag = "right"
        if self.rect_x >= 615:
            self.flag = "left"
        if self.flag == "left":
            self.rect_x -= self.speed
        else:
            self.rect_x += self.speed

class Wall():
    def __init__(self)

background = transform.scale(image.load('background.jpg'),(700,500))
clock = time.Clock()
FPS = 60
game = True
finish = False

Player = Player("hero.png", 5, 350, 4)
Treasure = GameSprite("treasure.png", 600, 400, 0)
Enemy = Enemy("cyborg.png", 420, 250, 0.5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game=False
    if game != False:
        window.blit(background,(0, 0))
        Player.reset()
        Enemy.reset()
        Player.update()
        Enemy.update()
        Treasure.reset()
        display.update()

clock.tick(FPS)